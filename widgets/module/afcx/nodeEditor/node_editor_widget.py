import sys

from PySide6.QtCore import QFile
from PySide6.QtGui import QBrush, Qt, QPen, QColor, QFont
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsView, QVBoxLayout, QGraphicsScene, QGraphicsItem, \
    QPushButton, QTextEdit
from widgets.module.afcx.nodeEditor import QNEGraphicsScene, QNEGraphicsView, Scene
from widgets.module.afcx.nodeEditor.node_edge import Edge, EDGE_TYPE_BEZIER
from widgets.module.afcx.nodeEditor.node_node import Node
from widgets.module.afcx.nodeEditor.node_socket import Socket


class NodeEditorWidget(QWidget):
    def __init__(self, parent=None):
        super(NodeEditorWidget, self).__init__(parent)

        self.stylesheet_filename = 'qss/nodestyle.qss'
        self.loadStyleSheet(self.stylesheet_filename)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # 创建graphics scene
        self.scene = Scene()
        # self.grScene = self.scene.grScene
        self.addNodes()

        # 创建graphics view
        self.view = QNEGraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)
        
        # self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("这是我的文字", QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        widget1 = QPushButton("hello world")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0, 30)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
        proxy2.setPos(0, 60)

        line = self.grScene.addLine(-200,-200, 400, -100, outlinePen)
        line.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsSelectable)

    def loadStyleSheet(self, filename):
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf-8'))
        print(filename)

    def addNodes(self):
        node1 = Node(self.scene, 'my node 1', inputs=[0, 0, 0], outputs=[1])
        node2 = Node(self.scene, 'my node 2', inputs=[3, 3, 3], outputs=[1])
        node3 = Node(self.scene, 'my node 3', inputs=[2, 2, 2], outputs=[1])
        node1.setPos(-350, -250)
        node2.setPos(-75, 0)
        node3.setPos(200, -150)

        edge1 = Edge(self.scene, node1.outputs[0], node2.inputs[0], edge_type=EDGE_TYPE_BEZIER)
        edge2 = Edge(self.scene, node2.outputs[0], node3.inputs[2], edge_type=EDGE_TYPE_BEZIER)



