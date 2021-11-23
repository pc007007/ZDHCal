from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from widgets.main.statusBarWidget.ui.statusWidget import Ui_statusWidget


class statusWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_statusWidget()
        self.ui.setupUi(self)

        self.ui.commandButton.clicked.connect(self.the_toggle_commandDock)
        self.ui.commandButton.setFlat(True)
        self.ui.commandButton.setCheckable(True)

    @Slot()
    def the_toggle_commandDock(self):
        mainWindow = self.parentWidget().parentWidget()
        visible = mainWindow.ui.dockWidget.isVisible()
        if visible:
            mainWindow.ui.dockWidget.setHidden(1)
            self.ui.commandButton.setChecked(False)
        else:
            mainWindow.ui.dockWidget.setHidden(0)
            self.ui.commandButton.setChecked(True)
