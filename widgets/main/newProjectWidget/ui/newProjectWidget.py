# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newProjectWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
                               QGridLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(268, 124)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"border-top:1px solid rgb(204,206,219);\n"
"border-left:1px solid rgb(204,206,219);\n"
"border-right:1px solid rgb(204,206,219);\n"
"padding:5px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(204,206,219)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.cancelPushButton = QPushButton(self.frame)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.gridLayout.addWidget(self.cancelPushButton, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.newPushButton = QPushButton(self.frame)
        self.newPushButton.setObjectName(u"newPushButton")

        self.gridLayout.addWidget(self.newPushButton, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.comboBox, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.newPushButton)
        QWidget.setTabOrder(self.newPushButton, self.cancelPushButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u9879\u76ee", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u9879\u76ee\u540d\u79f0", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88(&C)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"AFC\u8ba1\u7b97", None))

        self.newPushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a(&O)", None))
    # retranslateUi

