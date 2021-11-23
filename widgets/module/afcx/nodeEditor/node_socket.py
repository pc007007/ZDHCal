from collections import OrderedDict

from widgets.module.afcx.nodeEditor.node_graphics_socket import QNEGraphicsSocket
from widgets.module.afcx.nodeEditor.node_serializable import Serializable

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket(Serializable):
    def __init__(self, node, index=0, position=LEFT_TOP, socket_type=1, multi_edges=True):
        super().__init__()
        self.node = node
        self.index = index
        self.position = position
        self.socket_type = socket_type
        self.is_multi_edges = multi_edges

        self.grSocket = QNEGraphicsSocket(self, self.socket_type)

        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

        self.edges = []

    def __str__(self):
        return f'<Socket {hex(id(self))[2:5]}..{hex(id(self))[-3:]} {"ME" if self.is_multi_edges else "SE" }>'

    def getSocketPosition(self):
        res = self.node.getSocketPosition(self.index, self.position)
        return res

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeEdge(self, edge):
        if edge in self.edges: self.edges.remove(edge)
        else: print(f"!W: Socket::removeEdge wanna remove edge {edge} from self.edges but it's not in the list")

    # def hasEdge(self):
    #     return self.edges is not None

    def removeAllEdges(self):
        while self.edges:
            edge = self.edges.pop(0)
            edge.remove()
        # self.edges.clear()

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ('index', self.index),
            ('multi_edges', self.is_multi_edges),
            ('position', self.position),
            ('socket_type', self.socket_type),
        ])

    def deserialize(self, data, hashmap={}, restore_id=True):
        if restore_id: self.id = data['id']
        self.is_multi_edges = data['multi_edges']
        hashmap[data['id']] = self

        return True
