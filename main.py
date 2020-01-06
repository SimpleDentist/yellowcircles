import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.flag = False

        self.pushButton.clicked.connect(self.flagon)

    def flagon(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag is True:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp):
        qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        size = self.size()

        for i in range(15):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            circlesize = random.randint(1, 100)
            qp.drawEllipse(x, y, circlesize, circlesize)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())