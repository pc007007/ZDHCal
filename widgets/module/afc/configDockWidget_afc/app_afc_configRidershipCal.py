import json
from PySide6.QtCore import QFile, QUrl, Slot, Qt
from PySide6.QtGui import QDesktopServices, QFontMetrics, QResizeEvent
from PySide6.QtWidgets import QWidget
from widgets.module.afc.configDockWidget_afc.ui.Config_content_ridershipCal import Ui_ridershipCal


class Ridership_Config(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ridershipCal()
        self.ui.setupUi(self)

        self.ui.edit_btn.clicked.connect(self.slot_edit_ridership_by_excel)

    @Slot()
    def slot_edit_ridership_by_excel(self):
        """
        点击按钮启动外部程序运行文件
        :return:
        """
        filepath = self.ui.lineEdit.text()
        file = QFile(filepath)
        if file.exists():
            QDesktopServices.openUrl(QUrl.fromLocalFile(filepath))
        else:
            print("文件不存在")

    def loadFile(self, filePath):
        with open(filePath, 'r') as f: data = json.load(f)
        f.close()
        gatePara = [
            data['gate']['passRate'],
            data['gate']['peakTrainPairs'],
            data['gate']['minNum'],
            data['gate']['maxNum'],
        ]
        vendingMachinePara = [
            data['vendingMachine']['tktProcessingCap'],
            data['vendingMachine']['minNum'],
            data['vendingMachine']['rateOfRecentUse'],
            data['vendingMachine']['rateOfFutureUse'],
        ]
        ridershipAddress = data['ridershipAddress']

        self.ui.G1.setValue(gatePara[0])
        self.ui.G2.setValue(gatePara[1])
        self.ui.G3.setValue(gatePara[2])
        self.ui.G4.setValue(gatePara[3])

        self.ui.S1.setValue(vendingMachinePara[0])
        self.ui.S2.setValue(vendingMachinePara[1])
        self.ui.S3.setValue(vendingMachinePara[2])
        self.ui.S4.setValue(vendingMachinePara[3])

        self.ui.lineEdit.setText(ridershipAddress)
        self.ui.lineEdit.setToolTip(ridershipAddress)
        # ridershipAddress_s = QFontMetrics(self.ui.lineEdit.font()).elidedText(ridershipAddress, Qt.ElideRight, self.ui.lineEdit.width())
        # self.ui.lineEdit.setText(ridershipAddress_s)

