# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config_content_ridershipCal.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_ridershipCal(object):
    def setupUi(self, ridershipCal):
        if not ridershipCal.objectName():
            ridershipCal.setObjectName(u"ridershipCal")
        ridershipCal.setWindowModality(Qt.NonModal)
        ridershipCal.resize(327, 464)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ridershipCal.sizePolicy().hasHeightForWidth())
        ridershipCal.setSizePolicy(sizePolicy)
        ridershipCal.setFocusPolicy(Qt.StrongFocus)
        ridershipCal.setStyleSheet(u"QFrame#content{\n"
"	border:1px solid rgb(204,206,219);\n"
"	border-top:0px solid rgb(204,206,219);\n"
"	margin-bottom:0px;\n"
"}")
        self.verticalLayout = QVBoxLayout(ridershipCal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(ridershipCal)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"QFrame#content{\n"
"	background-color: rgb(245,245,245);\n"
"}\n"
"QWidget#scrollAreaWidgetContents_3{\n"
"	background-color: rgb(245,245,245);\n"
"}")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.content)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 325, 463))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(self.scrollAreaWidgetContents_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label, 6, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 13, 0, 1, 1)

        self.G2 = QSpinBox(self.frame)
        self.G2.setObjectName(u"G2")
        self.G2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.G2.setProperty("showGroupSeparator", False)
        self.G2.setSingleStep(0)

        self.gridLayout_3.addWidget(self.G2, 7, 1, 1, 4)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setBold(True)
        self.label_9.setFont(font)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 14, 0, 1, 1)

        self.G3 = QSpinBox(self.frame)
        self.G3.setObjectName(u"G3")
        self.G3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.G3.setProperty("showGroupSeparator", False)
        self.G3.setSingleStep(0)

        self.gridLayout_3.addWidget(self.G3, 8, 1, 1, 4)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 5)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_3.addWidget(self.label_11, 11, 0, 1, 5)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 12, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font)

        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)

        self.semi_machine = QSpinBox(self.frame)
        self.semi_machine.setObjectName(u"semi_machine")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.semi_machine.sizePolicy().hasHeightForWidth())
        self.semi_machine.setSizePolicy(sizePolicy1)
        self.semi_machine.setFrame(True)
        self.semi_machine.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.semi_machine.setMaximum(99)
        self.semi_machine.setSingleStep(0)
        self.semi_machine.setValue(2)

        self.gridLayout_3.addWidget(self.semi_machine, 4, 1, 1, 4)

        self.G1 = QSpinBox(self.frame)
        self.G1.setObjectName(u"G1")
        sizePolicy1.setHeightForWidth(self.G1.sizePolicy().hasHeightForWidth())
        self.G1.setSizePolicy(sizePolicy1)
        self.G1.setFrame(True)
        self.G1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.G1.setMaximum(99)
        self.G1.setSingleStep(0)

        self.gridLayout_3.addWidget(self.G1, 6, 1, 1, 4)

        self.S3 = QDoubleSpinBox(self.frame)
        self.S3.setObjectName(u"S3")
        self.S3.setDecimals(1)
        self.S3.setSingleStep(0.500000000000000)

        self.gridLayout_3.addWidget(self.S3, 14, 1, 1, 4)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 7, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 10, 0, 1, 5)

        self.S1 = QSpinBox(self.frame)
        self.S1.setObjectName(u"S1")
        sizePolicy1.setHeightForWidth(self.S1.sizePolicy().hasHeightForWidth())
        self.S1.setSizePolicy(sizePolicy1)
        self.S1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.S1.setSingleStep(0)

        self.gridLayout_3.addWidget(self.S1, 12, 1, 1, 4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 8, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 15, 0, 1, 1)

        self.S2 = QSpinBox(self.frame)
        self.S2.setObjectName(u"S2")
        self.S2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.S2.setSingleStep(0)

        self.gridLayout_3.addWidget(self.S2, 13, 1, 1, 4)

        self.G4 = QSpinBox(self.frame)
        self.G4.setObjectName(u"G4")
        self.G4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.G4.setProperty("showGroupSeparator", False)
        self.G4.setSingleStep(0)

        self.gridLayout_3.addWidget(self.G4, 9, 1, 1, 4)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 5)

        self.S4 = QDoubleSpinBox(self.frame)
        self.S4.setObjectName(u"S4")
        self.S4.setDecimals(1)
        self.S4.setSingleStep(0.500000000000000)

        self.gridLayout_3.addWidget(self.S4, 15, 1, 1, 4)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 9, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(8)
        self.lineEdit.setFont(font1)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.srcbutton = QPushButton(self.frame_2)
        self.srcbutton.setObjectName(u"srcbutton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.srcbutton.sizePolicy().hasHeightForWidth())
        self.srcbutton.setSizePolicy(sizePolicy3)
        self.srcbutton.setMinimumSize(QSize(0, 0))
        self.srcbutton.setMaximumSize(QSize(30, 16777215))
        self.srcbutton.setCheckable(False)

        self.horizontalLayout.addWidget(self.srcbutton)

        self.edit_btn = QPushButton(self.frame_2)
        self.edit_btn.setObjectName(u"edit_btn")

        self.horizontalLayout.addWidget(self.edit_btn)

        self.horizontalLayout.setStretch(0, 1)

        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 5)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.content)


        self.retranslateUi(ridershipCal)

        QMetaObject.connectSlotsByName(ridershipCal)
    # setupUi

    def retranslateUi(self, ridershipCal):
        ridershipCal.setWindowTitle(QCoreApplication.translate("ridershipCal", u"Form", None))
        self.label.setText(QCoreApplication.translate("ridershipCal", u"\u68c0\u7968\u673a\u901a\u8fc7\u7387(\u4eba/\u5206\u949f)     ", None))
        self.label_8.setText(QCoreApplication.translate("ridershipCal", u"\u6700\u5c0f\u914d\u7f6e\u8981\u6c42(\u53f0)", None))
        self.label_9.setText(QCoreApplication.translate("ridershipCal", u"\u5ba2\u6d41\u6570\u636e     ", None))
        self.label_6.setText(QCoreApplication.translate("ridershipCal", u"\u8fd1\u671f\u4f7f\u7528\u6bd4\u4f8b(%)", None))
        self.label_10.setText(QCoreApplication.translate("ridershipCal", u"\u81ea\u52a8\u68c0\u7968\u673a", None))
        self.label_11.setText(QCoreApplication.translate("ridershipCal", u"\u81ea\u52a8\u552e\u7968\u673a", None))
        self.label_5.setText(QCoreApplication.translate("ridershipCal", u"\u552e\u7968\u5904\u7406\u80fd\u529b(\u4eba/\u5206\u949f)     ", None))
        self.label_12.setText(QCoreApplication.translate("ridershipCal", u"\u534a\u81ea\u52a8\u552e\u7968\u673a    ", None))
        self.label_2.setText(QCoreApplication.translate("ridershipCal", u"\u9ad8\u5cf0\u5217\u8f66\u5bf9\u6570(\u5217/\u5c0f\u65f6)", None))
        self.label_3.setText(QCoreApplication.translate("ridershipCal", u"\u8fdb\u7ad9\u6700\u5c0f\u6570\u91cf(\u53f0\uff09", None))
        self.label_7.setText(QCoreApplication.translate("ridershipCal", u"\u8fdc\u671f\u4f7f\u7528\u6bd4\u4f8b(%)", None))
        self.label_4.setText(QCoreApplication.translate("ridershipCal", u"\u51fa\u7ad9\u6700\u5c0f\u6570\u91cf(\u53f0)", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ridershipCal", u"\u5bfc\u5165\u5ba2\u6d41\u8d44\u6599", None))
        self.srcbutton.setText(QCoreApplication.translate("ridershipCal", u"...", None))
        self.edit_btn.setText(QCoreApplication.translate("ridershipCal", u"\u7f16\u8f91", None))
    # retranslateUi

