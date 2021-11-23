from collections import OrderedDict

from widgets.module.afcx.nodeEditor.node_edge import Edge
from widgets.module.afcx.nodeEditor.node_graphics_edge import QNEGraphicsEdge
from widgets.module.afcx.nodeEditor.node_node import Node

DEBUG = False


class SceneClipboard():
    def __init__(self, scene):
        self.scene = scene

    def serializeSelected(self, delete=False):
        if DEBUG: print('-- COPY TO CLIPBOARD ---')

        sel_nodes, sel_edges, sel_sockets = [], [], {}

        # 对edges以及nodes排序
        for item in self.scene.grScene.selectedItems():
            if hasattr(item, 'node'):
                sel_nodes.append(item.node.serialize())
                for socket in (item.node.inputs + item.node.outputs):
                    sel_sockets[socket.id] = socket
            elif isinstance(item, QNEGraphicsEdge):
                sel_edges.append(item.edge)

        # debug
        if DEBUG:
            print("  NODES\n    ", sel_nodes)
            print("  EDGES\n    ", sel_edges)
            print("  SOCKETS\n    ", sel_sockets)

        # 移除所有没有链接到选中的node的edges
        edges_to_remove = []
        for edge in sel_edges:
            if edge.start_socket.id in sel_sockets and edge.end_socket.id in sel_sockets:
                # if DEBUG: print(" edge is ok, connected with both side")
                pass
            else:
                if DEBUG: print(f'edge:{edge} is not connected with both sides')
                edges_to_remove.append(edge)
        for edge in edges_to_remove:
            sel_edges.remove(edge)

        # make final list of edges
        edges_final = []
        for edge in sel_edges:
            edges_final.append(edge.serialize())

        data = OrderedDict([
            ('nodes', sel_nodes),
            ('edges', edges_final),
        ])

        # 如果
        if delete:
            self.scene.grScene.view()[0].deleteSelected()
            # 保存到history
            self.scene.history.storeHistory("Cut out elements from scene", setModified=True)

        return data

    def deserializeFromClipboard(self, data):
        hashmap = {}

        # 计算鼠标的指针 - scene的位置
        view = self.scene.grScene.views()[0]
        mouse_scene_pos = view.last_scene_mouse_position

        # 计算选中问题的bbox以及中心
        minx, maxx, miny, maxy = 0, 0, 0, 0
        for node_data in data['nodes']:
            x, y = node_data['pos_x'], node_data['pos_y']
            if x < minx: minx = x
            if x > maxx: maxx = x
            if y < miny: miny = y
            if y > maxy: maxy = y
        bbox_center_x = (minx + maxx) / 2
        bbox_center_y = (miny + maxy) / 2

        # center = view.mapToScene(view.rect().center())

        # 计算新nodes的偏移量
        offset_x = mouse_scene_pos.x() - bbox_center_x
        offset_y = mouse_scene_pos.y() - bbox_center_y

        # 创建每一个node
        for node_data in data['nodes']:
            new_node = Node(self.scene)
            new_node.deserialize(node_data, hashmap, restore_id=False)

            # 调整新的node的位置
            pos = new_node.pos
            new_node.setPos(pos.x() + offset_x, pos.y() + offset_y)

        # 创建每一个edge
        if 'edges' in data:
            for edge_data in data['edges']:
                new_edge = Edge(self.scene)
                new_edge.deserialize(edge_data, hashmap, restore_id=False)

        # 保存到history
        self.scene.history.storeHistory("Paste elements in scene.", setModified=True)
