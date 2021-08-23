from PyQt5.QtWidgets import QApplication, QMainWindow

from src.graphics.FootballField import FootballField


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.field = FootballField()
        self.setCentralWidget(self.field)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()