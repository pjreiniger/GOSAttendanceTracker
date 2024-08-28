from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
 
        idCodeBox = QLineEdit('Up')
        
        loginButton = QPushButton('Login')
        loginButton.clicked.connect(self.login)
         
        grid = QGridLayout()
        grid.addWidget(Button1, 0, 1)
        grid.addWidget(loginButton, 1, 1)
 
        self.setLayout(grid)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Practice Field Sign In')
        self.show()

    def login(self):
        print("Logging in!")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
