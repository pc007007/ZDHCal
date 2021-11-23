# coding:utf-8
from ctypes import POINTER, cast
from ctypes.wintypes import MSG

import win32api
import win32gui
import win32print
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication
# from win32 import win32api, win32gui
from win32.lib import win32con
from win32con import SM_CXSCREEN, SM_CYSCREEN

from widgets.main.mainWindow.windoweffect import WindowEffect, MINMAXINFO, NCCALCSIZE_PARAMS

DEBUG = False


class FramelessWindow(QWidget):

    BORDER_WIDTH = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__monitorInfo = None
        self.windowEffect = WindowEffect()
        # remove window border
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint |
                            Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        self.windowEffect.addShadowEffect(self.winId())
        self.resize(600, 600)

    def nativeEvent(self, eventType, message):
        """ Handle the Windows message """
        msg = MSG.from_address(message.__int__())
        if msg.message == win32con.WM_NCHITTEST:
            #  获取屏幕的缩放比
            win_ratio = QApplication.screens()[0].devicePixelRatio()
            # solve issue #2: the cursor is always in dragging state under multiple screens
            xPos = (win32api.LOWORD(msg.lParam)/win_ratio - self.frameGeometry().x()) % 65536
            yPos = win32api.HIWORD(msg.lParam)/win_ratio - self.frameGeometry().y()
            if DEBUG: print('x axis = ', win32api.LOWORD(msg.lParam), self.frameGeometry().x())
            if DEBUG: print('y axis = ', win32api.HIWORD(msg.lParam), self.frameGeometry().y())
            if DEBUG: print(f'x position:{xPos}, y position:{yPos}')
            w, h = self.width(), self.height()
            if DEBUG: print(f'宽度{w}, 高度{h}')
            lx = xPos < self.BORDER_WIDTH
            rx = xPos + 9 > w - self.BORDER_WIDTH
            ty = yPos < self.BORDER_WIDTH
            by = yPos > h - self.BORDER_WIDTH
            if lx and ty:
                return True, win32con.HTTOPLEFT
            elif rx and by:
                return True, win32con.HTBOTTOMRIGHT
            elif rx and ty:
                return True, win32con.HTTOPRIGHT
            elif lx and by:
                return True, win32con.HTBOTTOMLEFT
            elif ty:
                return True, win32con.HTTOP
            elif by:
                return True, win32con.HTBOTTOM
            elif lx:
                return True, win32con.HTLEFT
            elif rx:
                return True, win32con.HTRIGHT
        elif msg.message == win32con.WM_NCCALCSIZE:
            if self.__isWindowMaximized(msg.hWnd):
                self.__monitorNCCALCSIZE(msg)
            return True, 0
        elif msg.message == win32con.WM_GETMINMAXINFO:
            if self.__isWindowMaximized(msg.hWnd):
                window_rect = win32gui.GetWindowRect(msg.hWnd)
                if not window_rect:
                    return False, 0

                # get the monitor handle
                monitor = win32api.MonitorFromRect(window_rect)
                if not monitor:
                    return False, 0

                # get the monitor info
                __monitorInfo = win32api.GetMonitorInfo(monitor)
                monitor_rect = __monitorInfo['Monitor']
                work_area = __monitorInfo['Work']

                # convert lParam to MINMAXINFO pointer
                info = cast(msg.lParam, POINTER(MINMAXINFO)).contents

                # adjust the size of window
                info.ptMaxSize.x = work_area[2] - work_area[0]
                info.ptMaxSize.y = work_area[3] - work_area[1]
                info.ptMaxTrackSize.x = info.ptMaxSize.x
                info.ptMaxTrackSize.y = info.ptMaxSize.y

                # modify the upper left coordinate
                info.ptMaxPosition.x = abs(window_rect[0] - monitor_rect[0])
                info.ptMaxPosition.y = abs(window_rect[1] - monitor_rect[1])
                return True, 1

        return QWidget.nativeEvent(self, eventType, message)

    def __isWindowMaximized(self, hWnd) -> bool:
        """ Determine whether the window is maximized """
        # GetWindowPlacement() returns the display state of the window and the restored,
        # maximized and minimized window position. The return value is tuple
        windowPlacement = win32gui.GetWindowPlacement(hWnd)
        if not windowPlacement:
            return False

        return windowPlacement[1] == win32con.SW_MAXIMIZE

    def __monitorNCCALCSIZE(self, msg: MSG):
        """ Adjust the size of window """
        monitor = win32api.MonitorFromWindow(msg.hWnd)

        # If the display information is not saved, return directly
        if monitor is None and not self.__monitorInfo:
            return
        elif monitor is not None:
            self.__monitorInfo = win32api.GetMonitorInfo(monitor)

        # adjust the size of window
        params = cast(msg.lParam, POINTER(NCCALCSIZE_PARAMS)).contents
        params.rgrc[0].left = self.__monitorInfo['Work'][0]
        params.rgrc[0].top = self.__monitorInfo['Work'][1]
        params.rgrc[0].right = self.__monitorInfo['Work'][2]
        params.rgrc[0].bottom = self.__monitorInfo['Work'][3]

# class AcrylicWindow(FramelessWindow):
#     """ A frameless window with acrylic effect """
#
#     def __init__(self, parent=None):
#         super().__init__(parent=parent)
#         QtWin.enableBlurBehindWindow(self)
#         self.setWindowFlags(Qt.FramelessWindowHint |
#                             Qt.WindowMinMaxButtonsHint)
#         self.windowEffect.addWindowAnimation(self.winId())
#         self.windowEffect.setAcrylicEffect(self.winId())
#         self.setStyleSheet("background:transparent")
