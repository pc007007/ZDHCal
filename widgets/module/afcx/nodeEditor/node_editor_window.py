import json
import os

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel, QApplication, QMessageBox

from widgets.module.afcx.nodeEditor.node_editor_widget import NodeEditorWidget


class NodeEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.filename = None

        self.initUI()

    def createAct(self, name, shortcut, tooltip, callback):
        act = QAction(name, self)
        act.setShortcut(shortcut)
        act.setToolTip(tooltip)
        act.triggered.connect(callback)
        return act

    def initUI(self):
        menubar = self.menuBar()

        #  初始化Menu
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(self.createAct('新建(&N)', 'Ctrl+N', '创建新的图表', self.onFileNew))
        fileMenu.addSeparator()
        fileMenu.addAction(self.createAct('打开(&O)', 'Ctrl+O', '打开文件', self.onFileOpen))
        fileMenu.addAction(self.createAct('保存(&S)', 'Ctrl+S', '保存文件', self.onFileSave))
        fileMenu.addAction(self.createAct('另存为...', 'Ctrl+Shift+S', '文件另存为...', self.onFileSaveAs))
        fileMenu.addSeparator()
        fileMenu.addAction(self.createAct('退出(&Q)', 'Ctrl+Q', '退出程序', self.close))

        editMenu = menubar.addMenu('编辑(&E)')
        editMenu.addAction(self.createAct('撤销(&Z)', 'Ctrl+Z', '撤销上一次操作', self.onEditUndo))
        editMenu.addAction(self.createAct('恢复', 'Ctrl+Shift+Z', '恢复上次操作', self.onEditRedo))
        editMenu.addSeparator()
        editMenu.addAction(self.createAct('剪切(&X)', 'Ctrl+X', '剪裁到剪切板', self.onEditCut))
        editMenu.addAction(self.createAct('复制(&C)', 'Ctrl+C', '保存到剪切板', self.onEditCopy))
        editMenu.addAction(self.createAct('粘贴(&P)', 'Ctrl+V', '从剪切板复制', self.onEditPaste))
        editMenu.addSeparator()
        editMenu.addAction(self.createAct('删除', 'Ctrl+D', '删除选中的内容', self.onEditDelete))

        nodeEditor = NodeEditorWidget(self)
        nodeEditor.scene.addHasBeenModifiedListener(self.changeTitle)
        self.setCentralWidget(nodeEditor)

        #  status bar
        self.statusBar().showMessage('')
        self.status_mouse_pos = QLabel('')
        self.statusBar().addPermanentWidget(self.status_mouse_pos)
        nodeEditor.view.scenePosChanged.connect(self.onScenePosChanged)

        #  设定窗口属性
        self.setGeometry(200, 200, 1024, 768)
        self.changeTitle()
        self.show()

    def changeTitle(self):
        title = 'Node Editor - '
        if self.filename is None:
            title += 'New'
        else:
            title += os.path.basename(self.filename)

        if self.centralWidget().scene.has_been_modified:
            title += '*'

        self.setWindowTitle(title)

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def isModified(self):
        return self.centralWidget().scene.has_been_modified

    def maybeSave(self):
        if not self.isModified():
            return True

        res = QMessageBox.warning(self, '直接关闭?将会丢失内容!', '内容已经改变\n是否保存你的改动？',
                                  QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        if res == QMessageBox.Save:
            return self.onFileSave()
        elif res == QMessageBox.Cancel:
            return False

        return True

    def onScenePosChanged(self, x, y):
        self.status_mouse_pos.setText(f"场景坐标:[{x},{y}]")

    def onFileNew(self):
        if self.maybeSave():
            self.centralWidget().scene.clear()
            self.filename = None
            self.changeTitle()

    def onFileOpen(self):
        if self.maybeSave():
            fname, filter = QFileDialog.getOpenFileName(self, '从文件中打开图表')
            if fname == '':
                return
            if os.path.isfile(fname):
                self.centralWidget().scene.loadFromFile(fname)
                self.filename = fname
                self.changeTitle()

    def onFileSave(self):
        if self.filename is None: return self.onFileSaveAs()
        self.centralWidget().scene.saveToFile(self.filename)
        self.statusBar().showMessage(f"成功保存文件{self.filename}")
        return True

    def onFileSaveAs(self):
        fname, filter = QFileDialog.getSaveFileName(self, '保存图表到文件')
        if fname == '':
            return False
        self.filename = fname
        self.onFileSave()
        return True

    def onEditUndo(self):
        self.centralWidget().scene.history.undo()

    def onEditRedo(self):
        self.centralWidget().scene.history.redo()

    def onEditDelete(self):
        self.centralWidget().scene.grScene.views()[0].deleteSelected()\

    def onEditCut(self):
        data = self.centralWidget().scene.clipboard.serializeSelected(delete=True)
        str_data = json.dumps(data, indent=4)
        QApplication.instance().clipboard().setText(str_data)

    def onEditCopy(self):
        data = self.centralWidget().scene.clipboard.serializeSelected(delete=False)
        str_data = json.dumps(data, indent=4)
        QApplication.instance().clipboard().setText(str_data)

    def onEditPaste(self):
        raw_data = QApplication.instance().clipboard().text()
        try:
            data = json.loads(raw_data)
        except ValueError as e:
            print('粘贴的内容不是有效的Json数据', e)
            return

        #  检查json数据是否正确
        if 'nodes' not in data:
            print("JSON数据不包含任何的node内容")
            return

        self.centralWidget().scene.clipboard.deserializeFromClipboard(data)
