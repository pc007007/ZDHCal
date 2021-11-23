import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from widgets.Splash_Screen.main import ZDHSplashScreen
from widgets.main.mainWindow import Window
from tools.customWidget import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/resource/EDI-logo.svg"))

    # gif_address = u":/resource/giphy-1.gif"
    # splash = SplashScreen(gif_address)
    # splash.effect(app, delay_time=1)

    splashscreen = ZDHSplashScreen()

    # window = Window()
    # window.show()
    # splash.finish(window)

    sys.exit(app.exec())

