import json
from collections import OrderedDict

from widgets.module.afcx.nodeEditor import QNEGraphicsScene
from widgets.module.afcx.nodeEditor.node_edge import Edge
from widgets.module.afcx.nodeEditor.node_node import Node
from widgets.module.afcx.nodeEditor.node_scene_clipboard import SceneClipboard
from widgets.module.afcx.nodeEditor.node_scene_history import SceneHistory
from widgets.module.afcx.nodeEditor.node_serializable import Serializable


class Scene(Serializable):
    def __init__(self, parent=None):
        super().__init__()
        # super(Scene, self).__init__(parent)
        self.nodes = []
        self.edges = []
        self.scene_width = 64000
        self.scene_height = 64000

        self._has_been_modified = False
        self._has_been_modified_listeners = []

        self.initUI()
        self.history = SceneHistory(self)
        self.clipboard = SceneClipboard(self)

    @property
    def has_been_modified(self):
        # return False
        return self._has_been_modified
    @has_been_modified.setter
    def has_been_modified(self, value):
        if not self._has_been_modified and value:
            self._has_been_modified = value

            # call all registered listeners
            for callback in self._has_been_modified_listeners:
                callback()

        self._has_been_modified = value

    def addHasBeenModifiedListener(self, callback):
        self._has_been_modified_listeners.append(callback)

    def initUI(self):
        self.grScene = QNEGraphicsScene(self)
        self.grScene.setGrScene(self.scene_width, self.scene_height)

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeNode(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            print(f"!W: Scene::removeEdge wanna remove node {node} from self.nodes but it's not in the list")

    def removeEdge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
        else:
            print(f"!W: Scene::removeEdge wanna remove edge {edge} from self.edges but it's not in the list")

    def clear(self):
        while len(self.nodes) > 0:
            self.nodes[0].remove()

        self.has_been_modified = False

    def saveToFile(self, filename):
        with open(filename, 'w') as file:
            file.write(json.dumps(self.serialize(), indent=4))
            print("saving to", filename, "was successful.")

            self._has_been_modified = False

    def loadFromFile(self, filename):
        with open(filename, 'r') as file:
            raw_data = file.read()
            data = json.loads(raw_data)
            self.deserialize(data)

            self.has_been_modified = False

    def serialize(self):
        nodes, edges = [], []
        for node in self.nodes: nodes.append(node.serialize())
        for edge in self.edges: edges.append(edge.serialize())

        return OrderedDict([
            ('id', self.id),
            ('scene_width', self.scene_width),
            ('scene_height', self.scene_height),
            ('nodes', nodes),
            ('edges', edges),
        ])

    def deserialize(self, data, hashmap={}, restore_id=True):
        self.clear()
        hashmap = {}

        if restore_id: self.id = data['id']

        # ?????? nodes
        for node_data in data['nodes']:
            Node(self).deserialize(node_data, hashmap, restore_id)

        # ?????? edges
        for edge_data in data['edges']:
            Edge(self).deserialize(edge_data, hashmap, restore_id)

        return True
