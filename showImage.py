import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.im = QPixmap('pics/amg.png')
        self.label = QLabel()
        self.label.setPixmap(self.im)
        self.btn = QPushButton('Click Me')
        self.btn.clicked.connect(self.on_click)
        self.btn.show()
        self.grid.addWidget(self.label, 1, 0)
        self.setLayout(self.grid)
        self.grid = QGridLayout()


        self.setGeometry(50,50,3200,2000)
        self.setWindowTitle("PyQT show image")
        self.show()
    def on_click(self):
        self.label.setPixmap(QPixmap('pics/kmr.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Example()
    MainWindow.setCentralWidget(ui)
    MainWindow.show()
    sys.exit(app.exec_())