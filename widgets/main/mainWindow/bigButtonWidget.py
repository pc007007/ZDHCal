from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QToolButton

from widgets.main.mainWindow.ui.BigButton import Ui_BigButton


class BigButton(QToolButton):
    def __init__(self, parent=None):
        super(BigButton, self).__init__(parent=parent)

        self.ui = Ui_BigButton()
        self.ui.setupUi(self)

        self._title = self.ui.title_label
        self._description_line1 = self.ui.description_label_01
        self._description_line2 = self.ui.description_label_02

    def setTitle(self, title):
        self.ui.title_label.setText(title)
        self._title = title

    def getTitle(self):
        return self._title

    def setDescriptionL1(self, des):
        self.ui.description_label_01.setText(des)
        self._description_line1 = des

    def getDescriptionL1(self):
        return self._description_line1

    def setDescriptionL2(self, des):
        self.ui.description_label_02.setText(des)
        self._description_line2 = des

    def getDescriptionL2(self):
        return self._description_line2

    def setCustomIcon(self, icon: QIcon):
        self.ui.icon_button.setIcon(icon)

