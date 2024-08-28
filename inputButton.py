from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout
)
from PyQt6.QtCore import Qt
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("CodersLegacy")
 
        layout = QGridLayout()
        self.setLayout(layout)
 
        self.input = QLineEdit()
        self.input.setFixedWidth(150)
        self.input.returnPressed.connect(self.login)
        layout.addWidget(self.input, 0, 1)
 
        loginButton = QPushButton("Get Text")
        loginButton.clicked.connect(self.login)
        layout.addWidget(loginButton, 1,1)
 
        clearButton = QPushButton("Clear Text")
        clearButton.clicked.connect(self.input.clear)
        layout.addWidget(clearButton, 2, 1)
 
    def login(self):
        text = self.input.text()
        print(text)
        self.input.clear()
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
