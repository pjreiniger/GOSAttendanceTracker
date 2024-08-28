import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QGridLayout,
    QLineEdit,
    QVBoxLayout
    
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #super(QWidget, self).__init__(parent)

        self.setWindowTitle("Girls of Steel Meeting Login")

        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.resize(500,400)
        

        self.mainLoginTab = QWidget()
        self.outreachTab = QWidget()


        self.mainLoginTab.layout = QGridLayout()
        self.outreachTab.layout = QGridLayout()

        self.mainLoginTab.setLayout(self.mainLoginTab.layout)
        self.outreachTab.setLayout(self.outreachTab.layout)


        #Tab 1 content

        self.input = QLineEdit()
        self.input.setFixedWidth(150)
        self.input.returnPressed.connect(self.login)
        self.mainLoginTab.layout.addWidget(self.input, 0, 1)
 
        self.loginButton = QPushButton("Get Text")
        self.loginButton.clicked.connect(self.login)
        self.mainLoginTab.layout.addWidget(self.loginButton, 3,1)
 
        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.input.clear)
        self.mainLoginTab.layout.addWidget(self.clearButton, 4, 1)


        #Tab 2 Content

        self.label = QLabel("Page Under Construction")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.outreachTab.layout.addWidget(self.label)
        

        self.tabs.addTab(self.mainLoginTab, "Log Meeting")
        self.tabs.addTab(self.outreachTab, "Log Outreach")

        #self.setCentralWidget(self.tabs)
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

 
    def login(self):
        text = self.input.text()
        print(text)
        self.input.clear()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
