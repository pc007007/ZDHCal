import sys

from PySide6.QtWidgets import QApplication

from widgets.module.afcx.nodeEditor.node_editor_window import NodeEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    node_editor = NodeEditorWindow()
    # node_editor.show()

    sys.exit(app.exec())