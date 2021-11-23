from collections import OrderedDict

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

from widgets.module.afcx.nodeEditor.node_serializable import Serializable


class QNENodeContentWidget(QWidget, Serializable):
    def __init__(self, node, parent=None):
        self.node = node
        super(QNENodeContentWidget, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel('my widget')
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QNETextEdit('foo'))

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value

    def serialize(self):
        return OrderedDict([

        ])

    def deserialize(self, data, hashmap={}):
        return False


class QNETextEdit(QTextEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
