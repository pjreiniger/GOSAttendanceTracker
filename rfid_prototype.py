#read card
#access google sheets doc and check if user has signed in within the last 4 hours
#if not, ask what type of meeting they're there for
#add line to google sheet with their name, the date, and the meeting type


from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Practice Field Sign In")
        self.setWindowIcon(QIcon("icon.jpg"))
 
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
