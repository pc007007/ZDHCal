from PySide6.QtWidgets import QDialog, QFileDialog, QApplication
from PySide6.QtCore import Qt, Signal
from widgets.main.newProjectWidget.ui.newProjectWidget import Ui_Dialog
import json


class NewProjectDlg(QDialog):
    created = Signal(str,str)

    def __init__(self, mainwindow):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.newPushButton.clicked.connect(self.the_newPushButton_clicked)
        self.ui.cancelPushButton.clicked.connect(self.the_cancelPushButton_clicked)
        self.folder_path = ''
        self.ui.newPushButton.setDefault(1)
        self.mainwindow = mainwindow

    def the_newPushButton_clicked(self):
        filename = self.ui.lineEdit.text()
        if self.folder_path == '':
            filepath, _ = QFileDialog.getSaveFileName(
                self,
                '新建项目',
                filename,
                "AFC计算文件 (*.afc)"
            )
            if filepath != '':
                self.createJsonFile(filepath)
                self.close()
                self.created.emit(filepath, filename + ".afc")
                self.mainwindow.commdLine(f"创建文件[{filepath}]", showtime=True, color="#388e3c")
            else:
                print("地址为空")
        else:
            filepath = f"{self.folder_path}/{filename}.afc"
            self.createJsonFile(filepath)
            self.close()
            self.created.emit(filepath, filename + ".afc")
            self.mainwindow.commdLine(f"创建文件[{filepath}]", showtime=True, color="#388e3c")

    def the_cancelPushButton_clicked(self):
        self.close()

    def createJsonFile(self,filepath):
        with open(filepath,'a+') as f:
            json_data = {
                          "gate": {
                            "maxNum": 6,
                            "minNum": 4,
                            "passRate": 25,
                            "peakTrainPairs": 25
                          },
                          "ridershipAddress": "",
                          "vendingMachine": {
                            "minNum": 4,
                            "rateOfFutureUse": 10,
                            "rateOfRecentUse": 10,
                            "tktProcessingCap": 5
                          }
                        }
            f.write(json.dumps(json_data))

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos()-self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        # self.setCursor(QCursor(Qt.ArrowCursor))