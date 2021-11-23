import time

import win32con
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QToolBar
from win32gui import ReleaseCapture, SendMessage


class ToolBar(QToolBar):
    def __init__(self, *args, **kwargs):
        super(ToolBar, self).__init__(*args, **kwargs)
        self.back_to_normal_status = False
        self.m_flag = False
        self.m_Position = 0
        self.n = 0
        self.max_width = 0

    def mousePressEvent(self, event):
        """ Move the window """
        ReleaseCapture()
        SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,
                    win32con.SC_MOVE + win32con.HTCAPTION, 0)
        event.ignore()

    def mouseDoubleClickEvent(self, event):
        window = self.parent().parent()
        if window.isMaximized():
            window.showNormal()
            self.parent().main_title_widget.ui.full_btn.setIcon(QIcon(":/resource/ChromeMaximize_16x.svg"))
            self.parent().main_title_widget.ui.full_btn.setToolTip("最大化")

        else:
            window.showMaximized()
            self.parent().main_title_widget.ui.full_btn.setIcon(QIcon(":/resource/ChromeRestore_16x.svg"))
            self.parent().main_title_widget.ui.full_btn.setToolTip("还原")

