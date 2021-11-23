################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
import _thread
import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

## ==> SPLASH SCREEN


## ==> MAIN WINDOW
# from ui_main import Ui_MainWindow

## ==> GLOBALS
from widgets.Splash_Screen.ui_splash_screen import Ui_SplashScreen
from widgets.main.mainWindow import Window

counter = 0

# # YOUR APPLICATION
# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         # MAIN WINDOW LABEL
#         QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
#         QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))


# SPLASH SCREEN
class ZDHSplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>欢迎</strong> 使用软件！")

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_description.setText("<strong>载入</strong> 后台数据..."))
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_description.setText("<strong>载入</strong> 用户界面..."))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.window = Window()
            self.window.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 4




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZDHSplashScreen()
    sys.exit(app.exec_())