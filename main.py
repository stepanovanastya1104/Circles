import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)
        self.show_btn.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        x = random.randrange(450)
        y = random.randrange(450)
        qp.setBrush(QColor(254, 220, 3))
        a = random.randrange(400)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())