from PySide6.QtWidgets import QWidget
from widgets.main.dockTitleWidget.ui.myDockTitleWidget import Ui_myDockTitleWidget


class myDockTitleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_myDockTitleWidget()
        self.ui.setupUi(self)

        self.ui.closeBtn.clicked.connect(self.closeDock)
        # self.ui.flotBtn.toggled.connect(self.flowDock)
        self.ui.flotBtn.setCheckable(True)
        self.ui.flotBtn.toggled.connect(lambda checked: self.parent().setFloating(checked))

    def closeDock(self):
        dock = self.parentWidget()
        title = self.ui.title.text()
        if title == '命令行':
            main_window = self.parentWidget().parentWidget()
            main_window.status_bar.the_toggle_commandDock()
        else:
            dock.close()
        dock.close()

    def setTitle(self, title):
        self.ui.title.setText(title)
