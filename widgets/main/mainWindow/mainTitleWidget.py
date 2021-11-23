from PySide6.QtWidgets import QWidget

from widgets.main.mainWindow.ui.main_title_widget import Ui_mainTitleWidget


class MainTitleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainTitleWidget, self).__init__(*args, **kwargs)
        self.ui = Ui_mainTitleWidget()
        self.ui.setupUi(self)

    def setTitle(self, title):
        self.ui.title_btn.setText(title)

