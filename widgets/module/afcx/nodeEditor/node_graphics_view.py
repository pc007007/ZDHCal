from PySide6.QtCore import QEvent, Signal
from PySide6.QtGui import QPainter, Qt, QMouseEvent, QWheelEvent
from PySide6.QtWidgets import QGraphicsView, QApplication

from widgets.module.afcx.nodeEditor.node_edge import EDGE_TYPE_BEZIER, Edge
from widgets.module.afcx.nodeEditor.node_graphics_cutline import QNECutLine
from widgets.module.afcx.nodeEditor.node_graphics_edge import QNEGraphicsEdge
from widgets.module.afcx.nodeEditor.node_graphics_socket import QNEGraphicsSocket

MODE_NOOP = 1
MODE_EDGE_DRAG = 2
MODE_EDGE_CUT = 3

EDGE_DRAG_START_THRESHOLD = 10
DEBUG = True


class QNEGraphicsView(QGraphicsView):
    scenePosChanged = Signal(int, int)

    def __init__(self, grScene, parent=None):
        super(QNEGraphicsView, self).__init__(parent=parent)
        self.grScene = grScene

        self.initUI()

        self.setScene(self.grScene)

        self.mode = MODE_NOOP
        self.editingFlag = False
        self.rubberBandDraggingRectangle = False

        self.zoomInFactor = 1.25    # 缩放系数
        self.zoomClamp = True       # 缩放是否有限制
        self.zoom = 10               # 当前缩放比例
        self.zoomStep = 1           # 缩放步数
        self.zoomRange = [0, 10]    # 缩放范围

        # cutline
        self.cutline = QNECutLine()
        self.grScene.addItem(self.cutline)

    def initUI(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 基于鼠标位置进行变换
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.setDragMode(QGraphicsView.RubberBandDrag)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event):
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(),
                                   Qt.LeftButton, Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event):
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                Qt.LeftButton, event.buttons() & Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.RubberBandDrag)

    def leftMouseButtonPress(self, event):
        # 获取点击的item
        item = self.getItemAtClick(event)

        # 保存最后左键点击的位置
        self.last_lmb_click_scene_pos = self.mapToScene(event.pos())

        # if DEBUG: print("LMB Click on", item, self.debug_modifiers(event))
        # 逻辑
        if hasattr(item, "node") or isinstance(item, QNEGraphicsEdge) or item is None:
            if event.modifiers() & Qt.ShiftModifier:
                event.ignore()
                fakeEvent = QMouseEvent(QEvent.MouseButtonPress, event.localPos(), event.screenPos(),
                                        Qt.LeftButton, event.button() | Qt.LeftButton,
                                        event.modifiers() | Qt.ControlModifier)
                super(QNEGraphicsView, self).mousePressEvent(fakeEvent)
                return

        if type(item) is QNEGraphicsSocket:
            if self.mode == MODE_NOOP:
                self.mode = MODE_EDGE_DRAG
                self.edgeDragStart(item)
                return

        if self.mode == MODE_EDGE_DRAG:
            res = self.edgeDragEnd(item)
            if res: return

        if item is None:
            if event.modifiers() & Qt.ControlModifier:
                self.mode = MODE_EDGE_CUT
                fakeEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(),
                                        Qt.LeftButton, Qt.NoButton, event.modifiers())
                super().mouseReleaseEvent(fakeEvent)
                QApplication.setOverrideCursor(Qt.CrossCursor)
                return
            else:
                self.rubberBandDraggingRectangle = True

        super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        # 获取点击的item
        item = self.getItemAtClick(event)

        # 逻辑
        if hasattr(item, "node") or isinstance(item, QNEGraphicsEdge) or item is None:
            if event.modifiers() & Qt.ShiftModifier:
                event.ignore()
                fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                        Qt.LeftButton, Qt.NoButton,
                                        event.modifiers() | Qt.ControlModifier)
                super(QNEGraphicsView, self).mouseReleaseEvent(fakeEvent)
                return

        if self.mode == MODE_EDGE_DRAG:
            if self.distanceBetweenClickAndReleaseIsOff(event):
                res = self.edgeDragEnd(item)
                if res: return

        if self.mode == MODE_EDGE_CUT:
            self.cutIntersectingEdges()
            self.cutline.line_points = []
            self.cutline.update()
            QApplication.setOverrideCursor(Qt.ArrowCursor)
            self.mode = MODE_NOOP
            return

        # if self.dragMode() == QGraphicsView.RubberBandDrag:
        if self.rubberBandDraggingRectangle:
            self.grScene.scene.history.storeHistory('Selection changed')
            self.rubberBandDraggingRectangle = False

        super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self, event):
        super().mousePressEvent(event)

        item = self.getItemAtClick(event)
        if DEBUG:
            if isinstance(item, QNEGraphicsEdge): print('RMB DEBUG:', item.edge, 'connection sockets:',
                                                        item.edge.start_socket, '<-->', item.edge.end_socket)
            if type(item) is QNEGraphicsSocket: print('RMB DEBUG:', item.socket, 'has edge', item.socket.edges)
            if item is None:
                print('SCENE:')
                print('  Nodes:')
                for node in self.grScene.scene.nodes: print('    ', node)
                print(' Edges:')
                for edge in self.grScene.scene.edges: print('    ', edge)

    def rightMouseButtonRelease(self, event):
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.mode == MODE_EDGE_DRAG:
            pos = self.mapToScene(event.pos())
            self.drag_edge.grEdge.setDestination(pos.x(), pos.y())
            self.drag_edge.grEdge.update()

        if self.mode == MODE_EDGE_CUT:
            pos = self.mapToScene(event.pos())
            self.cutline.line_points.append(pos)
            self.cutline.update()

        self.last_scene_mouse_position = self.mapToScene(event.pos())
        self.scenePosChanged.emit(
            int(self.last_scene_mouse_position.x()),
            int(self.last_scene_mouse_position.y()),
        )

        super().mouseMoveEvent(event)

    def keyPressEvent(self, event):
        # if event.key() == Qt.Key_Delete:
        #     if not self.editingFlag:
        #         self.deleteSelected()
        #     else:
        #         super().keyPressEvent(event)
        # elif event.key() == Qt.Key_S and event.modifiers() & Qt.ControlModifier:
        #     self.grScene.scene.saveToFile('graph.json.txt')
        # elif event.key() == Qt.Key_L and event.modifiers() & Qt.ControlModifier:
        #     self.grScene.scene.loadFromFile('graph.json.txt')
        # elif event.key() == Qt.Key_Z and event.modifiers() & Qt.ControlModifier and not event.modifiers() & Qt.ShiftModifier:
        #     self.grScene.scene.history.undo()
        # elif event.key() == Qt.Key_Z and event.modifiers() & Qt.ControlModifier and event.modifiers() & Qt.ShiftModifier:
        #     self.grScene.scene.history.redo()
        # elif event.key() == Qt.Key_H:
        #     print(f'HISTORY: len({len(self.grScene.scene.history.history_stack)}) '
        #           f'-- current_step {self.grScene.scene.history.history_current_step}')
        #     for ix, item in enumerate(self.grScene.scene.history.history_stack):
        #         print(f'#{ix}--{item["desc"]}')
        # else:
        super().keyPressEvent(event)

    def cutIntersectingEdges(self):
        for ix in range(len(self.cutline.line_points) - 1):
            p1 = self.cutline.line_points[ix]
            p2 = self.cutline.line_points[ix + 1]

            for edge in self.grScene.scene.edges:
                if edge.grEdge.intersectsWith(p1,p2):
                    edge.remove()
        self.grScene.scene.history.storeHistory('Delete cutted edges', setModified=True)

    def deleteSelected(self):
        for item in self.grScene.selectedItems():
            if isinstance(item, QNEGraphicsEdge):
                item.edge.remove()
            elif hasattr(item, 'node'):
                item.node.remove()
        self.grScene.scene.history.storeHistory('Delete selected', setModified=True)

    def debug_modifiers(self, event):
        out = "MODS:"
        if event.modifiers() & Qt.ShiftModifier: out += "SHIFT "
        if event.modifiers() & Qt.ControlModifier: out += "CTRL "
        if event.modifiers() & Qt.AltModifier: out += "ALT "
        return out

    def wheelEvent(self, event):
        # 计算缩放系数
        zoomOutFactor = 1/self.zoomInFactor

        # 计算zoom
        if event.angleDelta().y() > 0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        clamped = False
        if self.zoom < self.zoomRange[0]:
            self.zoom, clamped = self.zoomRange[0], True
        if self.zoom > self.zoomRange[1]:
            self.zoom, clamped = self.zoomRange[1], True

        # 设定scene的比列
        if not clamped or self.zoomClamp is False:
            self.scale(zoomFactor, zoomFactor)

    def getItemAtClick(self, event):
        """获取点击的item"""
        pos = event.pos()
        obj = self.itemAt(pos)
        return obj

    def edgeDragStart(self, item):
        if DEBUG: print('View::edgeDragStart - Start dragging edge')
        if DEBUG: print('View::edgeDragStart -   assign Start Socket to:', item.socket)
        # self.previousEdge = item.socket.edges
        self.drag_start_socket = item.socket
        self.drag_edge = Edge(self.grScene.scene, item.socket, None, EDGE_TYPE_BEZIER)
        if DEBUG: print('View::edgeDragStart -   dragEdge:', self.drag_edge)

    def edgeDragEnd(self, item):
        """返回True跳过其余代码"""
        self.mode = MODE_NOOP

        if DEBUG: print('View::edgeDragEnd - End dragging edge')
        self.drag_edge.remove()
        self.drag_edge = None

        if type(item) is QNEGraphicsSocket:
            if item.socket != self.drag_start_socket:
                # if we released dragging on a socket (other then the beginning socket)
                # if DEBUG: print('View::edgeDragEnd -  previous edge:', self.previousEdge)
                # if item.socket.hasEdge():
                #     item.socket.edges.remove()
                # for edge in item.socket.edges:
                #     edge.remove()
                if not item.socket.is_multi_edges:
                    item.socket.removeAllEdges()
                # we wanna keep all the edges coming from start socket
                if not self.drag_start_socket.is_multi_edges:
                    self.drag_start_socket.removeAllEdges()
                # if DEBUG: print('View::edgeDragEnd -  assignEnd Socket', item.socket)
                # if self.previousEdge is not None: self.previousEdge.remove()
                # if DEBUG: print('View::edgeDragEnd - previous edge removed')
                # self.drag_edge.start_socket = self.drag_start_socket
                # self.drag_edge.end_socket = item.socket
                # self.drag_edge.start_socket.addEdge(self.drag_edge)
                # self.drag_edge.end_socket.addEdge(self.drag_edge)
                # if DEBUG: print('View::edgeDragEnd -  reassigned start & end sockets to drag edge')
                # self.drag_edge.updatePositions()
                self.grScene.scene.history.storeHistory('Created new edge by dragging', setModified=True)
                new_edge = Edge(self.grScene.scene, self.drag_start_socket, item.socket, edge_type=EDGE_TYPE_BEZIER)
                if DEBUG: print(f'View::edgeDragEnd - created new edge: {new_edge} connectiong {new_edge.start_socket} <--> {new_edge.end_socket}')

                return True

        # if DEBUG: print('View::edgeDragEnd - END dragging edge')
        # if DEBUG: print('View::edgeDragEnd - about to set socket to previous edge:', self.previousEdge)
        # if self.previousEdge is not None:
        #     self.previousEdge.start_socket.edges = self.previousEdge
        if DEBUG: print('View::edgeDragEnd - everything done.')

        return False

    def distanceBetweenClickAndReleaseIsOff(self, event):
        """ 测量是否移动了足够的距离"""
        new_lmb_release_scene_pos = self.mapToScene(event.pos())
        dist_scene = new_lmb_release_scene_pos - self.last_lmb_click_scene_pos
        edge_drag_threshold_sq = EDGE_DRAG_START_THRESHOLD * EDGE_DRAG_START_THRESHOLD
        return (dist_scene.x() * dist_scene.x() + dist_scene.y() * dist_scene.y()) > edge_drag_threshold_sq


