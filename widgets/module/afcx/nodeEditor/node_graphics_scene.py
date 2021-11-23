import math

from PySide6.QtCore import QLine
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView


class QNEGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super(QNEGraphicsScene, self).__init__(parent)

        self.scene = scene

        # 设置
        self.gridSize = 20
        self.gridSquares = 5

        self._color_background = QColor("#393939")  # 背景色
        self._color_light = QColor('#2f2f2f')       # 背景线条颜色-浅
        self._color_dark = QColor('#292929')        # 背景线条颜色-深

        # # 浅色背景
        # self._color_background = QColor(255, 255, 255)
        # self._color_light = QColor(228, 228, 228)
        # self._color_dark = QColor(218, 218, 218)

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        self.setBackgroundBrush(self._color_background)

    def setGrScene(self, width, height):
        self.setSceneRect(-width // 2, -height / 2, width, height)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        # 1.这里创建我们的Grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        # 2.计算所有需要画的线
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.gridSize):
            if x % (self.gridSize*self.gridSquares) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            if y % (self.gridSize*self.gridSquares) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        # 3.画线
        painter.setPen(self._pen_light)
        painter.drawLines(lines_light)

        painter.setPen(self._pen_dark)
        painter.drawLines(lines_dark)
