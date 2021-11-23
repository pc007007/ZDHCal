from PySide6.QtGui import Qt, QBrush, QPen, QPainter
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QHBoxLayout, QGraphicsItem


class ViewEditor(QWidget):
    def __init__(self, parent=None):
        super(ViewEditor, self).__init__(parent=parent)

        self.layout = QHBoxLayout(self)
        self.scene = QGraphicsScene()
        self.graphicView = QGraphicsView(self.scene, self)
        self.layout.addWidget(self.graphicView)
        self.createGraphicView()

    def createGraphicView(self):
        # 设置视图的抗锯齿模式
        self.graphicView.setRenderHint(QPainter.Antialiasing)

        greenBrush = QBrush(Qt.green)
        grayBrush = QBrush(Qt.gray)
        pen = QPen(Qt.red)
        ellipse = self.scene.addEllipse(20, 20, 200, 200, pen, greenBrush)
        rect = self.scene.addRect(-100, -100, 200, 200, pen, grayBrush)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsSelectable)


