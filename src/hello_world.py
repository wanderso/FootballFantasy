from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Hello world!")
        canvas = QPixmap(400, 300)
        canvas.fill(QColor("grey"))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.draw_something()

    def draw_something(self):
        from random import randint, choice
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']

        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            # pen = painter.pen() you could get the active pen here
            pen.setColor(QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + randint(-100, 100),  # x
                150 + randint(-100, 100)  # y
            )
        painter.end()


app = QApplication([])
window = MainWindow()
window.show()

app.exec()