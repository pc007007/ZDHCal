from widgets.module.afcx.nodeEditor.node_graphics_edge import QNEGraphicsEdge

DEBUG = False


class SceneHistory():
    def __init__(self, scene):
        self.scene = scene

        self.history_stack = []
        self.history_current_step = -1
        self.history_limit = 32

    def undo(self):
        if DEBUG: print('UNDO')
        if self.history_current_step > 0:
            self.history_current_step -= 1
            self.restoreHistory()

    def redo(self):
        if DEBUG: print('REDO')
        if self.history_current_step + 1 < len(self.history_stack):
            self.history_current_step += 1
            self.restoreHistory()

    def restoreHistory(self):
        if DEBUG: print(f'Restoring history .... current_step: @{self.history_current_step} ({ len(self.history_stack)})')
        self.restoreHistoryStamp(self.history_stack[self.history_current_step])

    def storeHistory(self, desc, setModified=False):
        if setModified:
            self.scene.has_been_modified = True

        if DEBUG: print(f'Storing history "{desc}" .... current_step: {self.history_current_step}({len(self.history_stack)})')
        hs = self.createHistoryStamp(desc)

        # 如果history_current_step的指针不在history_stack的末尾
        if self.history_current_step + 1 < len(self.history_stack):
            self.history_stack = self.history_stack[0:self.history_current_step+1]

        #  历史信息如果超过设定的最大数量
        if self.history_current_step + 1 >= self.history_limit:
            self.history_stack = self.history_stack[1:]
            self.history_current_step -= 1

        self.history_stack.append(hs)
        self.history_current_step += 1
        if DEBUG: print(' -- setting setp to:', self.history_current_step)

    def createHistoryStamp(self, desc):
        sel_obj = {
            'nodes': [],
            'edges': [],
        }
        for item in self.scene.grScene.selectedItems():
            if hasattr(item, 'node'):
                sel_obj['nodes'].append(item.node.id)
            elif isinstance(item, QNEGraphicsEdge):
                sel_obj['edges'].append(item.edge.id)

        history_stamp = {
            'desc': desc,
            'snapshot': self.scene.serialize(),
            'selection': sel_obj,
        }
        return history_stamp

    def restoreHistoryStamp(self, history_stamp):
        if DEBUG: print('RHS:', history_stamp['desc'])

        self.scene.deserialize(history_stamp['snapshot'])

        #  恢复selection的指示
        for edge_id in history_stamp['selection']['edges']:
            for edge in self.scene.edges:
                if edge_id == edge_id:
                    edge.grEdge.setSelected(True)
                    break

        for node_id in history_stamp['selection']['nodes']:
            for node in self.scene.nodes:
                if node.id == node_id:
                    node.grNode.setSelected(True)
                    break