from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

class ym12s(QLabel):
    def __init__(self, fileAnh, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(fileAnh)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing) 
        painter.setRenderHint(QPainter.SmoothPixmapTransform) 
        pixmap_minimize = self.pixmap.scaled(self.size(), 
                        Qt.KeepAspectRatioByExpanding, 
                        Qt.SmoothTransformation)
        path = QPainterPath()
        boTron = 30
        path.addRoundedRect(0, 0, self.width(), self.height(), boTron, boTron)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, self.width(), self.height(), pixmap_minimize)

    def resizeEvent(self, event):
        self.update()  
        super().resizeEvent(event)
        
  