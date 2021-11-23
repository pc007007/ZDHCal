from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor, QPen, QBrush
from PySide6.QtWidgets import QGraphicsItem


class QNEGraphicsSocket(QGraphicsItem):
    def __init__(self, socket=None, socket_type=1):
        super(QNEGraphicsSocket, self).__init__(socket.node.grNode)

        self.socket = socket
        self.radius = 6.0
        self.outline_width = 1.0
        self._colors = [
            QColor('#FFFF7700'),
            QColor('#FF52e220'),
            QColor('#FF0056a6'),
            QColor('#FFa86db1'),
            QColor('#FFb54747'),
            QColor('#FFdbe220')
        ]

        self._color_background = self._colors[socket_type]
        self._color_outline = QColor('#FF000000')

        self._pen = QPen(self._color_outline)
        self._pen.setWidth(self.outline_width)
        self._brush = QBrush(self._color_background)

    def paint(self, painter, QStyleOptionGraphicsItem, Widget=None) -> None:
        # 画圆型
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius, -self.radius, 2*self.radius, 2*self.radius)

    def boundingRect(self):
        return QRectF(
            - self.radius - self.outline_width,
            - self.radius - self.outline_width,
            2 * (self.radius + self.outline_width),
            2 * (self.radius + self.outline_width)
        )
