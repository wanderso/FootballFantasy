from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import QPoint


class FootballField(QLabel):
    def __init__(self):
        super().__init__()

        self.window_length = 200*6
        self.window_width = 500*6

        self.field_length = 160*6           # 160 feet - NFL Rulebook §§1-1-1-¶1
        self.field_width = 360*6            # 360 feet - NFL Rulebook §§1-1-1-¶1

        self.field_border = 6*6             # 6 foot-long unbroken white border around field - §§1-1-2-¶1

        self.line_width = 2                 # 4 inches wide - NFL Rulebook Page 5, 'Field Markings', §2

        canvas = QPixmap(self.window_width, self.window_length)
        canvas.fill(QColor("green"))
        self.setPixmap(canvas)
        self.paint_boundary()
        self.paint_goal_lines()
        self.paint_yard_lines()

    def paint_boundary(self):
        painter = QPainter(self.pixmap())
        pen = QPen()
        pen.setWidth(self.field_border)
        pen.setColor(QColor("white"))
        painter.setPen(pen)
        painter.drawRect(50, 50, self.field_width, self.field_length)
        painter.end()

    def paint_goal_lines(self):
        painter = QPainter(self.pixmap())
        pen = QPen()
        pen.setWidth(self.line_width*2)     # Goal lines have double width - NFL Rulebook Page 5, 'Field Markings', §2
        pen.setColor(QColor("white"))
        painter.setPen(pen)

        painter.drawLine(
            QPoint(50+(6*30), 50),
            QPoint(50+(6*30), 50+self.field_length)
        )

        painter.drawLine(
            QPoint(50+self.field_width-(6*30), 50),
            QPoint(50+self.field_width-(6*30), 50+self.field_length)
        )

        painter.end()

    def paint_yard_lines(self):
        painter = QPainter(self.pixmap())
        pen = QPen()
        pen.setWidth(self.line_width)
        pen.setColor(QColor("white"))
        painter.setPen(pen)

        for i in range(1, 11):
            painter.drawLine(
                QPoint(50 + (i*(6 * 30)), 50),
                QPoint(50 + (i*(6 * 30)), 50 + self.field_length)
            )

        painter.end()







