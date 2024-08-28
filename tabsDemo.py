#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------

import sys

import gspread

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QLabel,
    QApplication
)

from PyQt6.QtGui import QIcon, QPixmap, QFont

from PyQt6.QtCore import pyqtSlot, Qt, QObject, QThread, pyqtSignal

import datetime as dt


#-----------------------------------------------------------------------
# GLOBAL VARIABLES
#-----------------------------------------------------------------------

SPREADSHEET_KEY = "163-AIfY7czQUz-1WUggts3lUEXNV6TebKseutOeIeDI"
WIDTH = 800
HEIGHT = 400



#-----------------------------------------------------------------------
# USER INTERFACE CODE
#-----------------------------------------------------------------------
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Girls of Steel Meeting Login'
        self.left = 0
        self.top = 0
        self.width = WIDTH
        self.height = HEIGHT
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #ff837a; font-size: 20pt;")
        self.showMaximized()
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()

##class Worker(QThread):
##    finished = pyqtSignal()
##    progress = pyqtSignal(str)
##
####    def _init_(self):
####        QThread._init_(self)
####
####    def _del_(self):
####        self.wait()
##
##    
##    
##
##    def logAttendance(self,SK, name, ID):
##        self.progress.emit("Logging in...")
##        sh = gc.open_by_key(SK)
##        wl = sh.worksheets()
##        date = dt.datetime.now()
##        ds = wl[0]
##        ds.append_row([date.strftime('%c'), ID, name, "General Meeting"])
##        self.finished.emit()
##
####    def run(self):
####        
####        """Long-running task."""
####        for i in range(5):
####            sleep(1)
####            self.progress.emit(i + 1)
####        self.finished.emit()
    

    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(WIDTH,HEIGHT)

##        QWidget#tab1:pressed {
##    background-color: rgb(224, 0, 0);
##    border-style: inset;
##}
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Log Attendance")
        self.tabs.addTab(self.tab2,"Lookup Fob Number")
        self.tabs.addTab(self.tab3,"Identify Fob")

        #self.tabs.setStyleSheet("QTabBar::tab { height: 150px;")#background-color: #ffffff;}")

        #--------------------
        # Tab 1 Content
        #--------------------
        self.tab1.layout = QGridLayout(self)
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.setStyleSheet("background-color: #bad3fe;")
        

        self.logo = QLabel(self)
        self.pixmap = QPixmap('logo3.png')
        self.logo.setPixmap(self.pixmap)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab1.layout.addWidget(self.logo, 0,1)

        self.header = QLabel("Log your attendance at today's GoS meeting!")
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        headerFont = QFont()
        headerFont.setBold(True)
        self.header.setFont(headerFont)
        self.header.setStyleSheet("font-size: 35pt;")
        self.tab1.layout.addWidget(self.header, 1,1)

        self.instructions = QLabel("Tap your fob to the reader to log in, or type in the number associated with your fob.\nIt may take a second or two for the log in to process.")
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions.setStyleSheet("font-size: 25pt;")
        self.tab1.layout.addWidget(self.instructions, 2,1)

        self.inputArea = QWidget()
        self.inputArea.layout = QGridLayout(self)
        self.inputArea.setLayout(self.inputArea.layout)
        self.tab1.layout.addWidget(self.inputArea,3,1)

        self.input = QLineEdit()
        self.input.setFixedWidth(250)
        self.input.setFixedHeight(40)
        self.input.setStyleSheet("font-size: 25pt;")
        self.input.returnPressed.connect(self.login)
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inputArea.layout.addWidget(self.input, 0, 1)
 
        self.loginButton = QPushButton("Login")
        self.loginButton.setStyleSheet("font-size: 25pt;")
        self.loginButton.clicked.connect(self.login)
        self.inputArea.layout.addWidget(self.loginButton, 1,1)
 
        self.clearButton = QPushButton("Clear")
        self.clearButton.setStyleSheet("font-size: 25pt;")
        self.clearButton.clicked.connect(self.input.clear)
        self.clearButton.clicked.connect(
            lambda: self.message.setText("")
        )
        self.inputArea.layout.addWidget(self.clearButton, 2, 1)

        self.message = QLabel("")
        self.message.setStyleSheet("font-size: 25pt;")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab1.layout.addWidget(self.message, 4, 1)

        #--------------------
        #Tab 2 Content
        #--------------------
##        self.tab2.layout = QVBoxLayout(self)
##        self.tab2.setLayout(self.tab2.layout)
##        self.label = QLabel("Page Under Construction")
##        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
##        self.tab2.layout.addWidget(self.label)

        self.tab2.layout = QGridLayout(self)
        self.tab2.setLayout(self.tab2.layout)
        self.tab2.setStyleSheet("background-color: #bad3fe;")#ffc3bf;")

        self.header2 = QLabel("Forgot your fob? Not a problem!")
        self.header2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header2.setFont(headerFont)
        self.header2.setStyleSheet("font-size: 35pt;")
        self.tab2.layout.addWidget(self.header2, 1,1)

        self.instructions2 = QLabel("Type your full name below. (Ex: Rosie Riveter)")
        self.instructions2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions2.setStyleSheet("font-size: 25pt;")
        self.tab2.layout.addWidget(self.instructions2, 2,1)

        self.inputArea2 = QWidget()
        self.inputArea2.layout = QGridLayout(self)
        self.inputArea2.setLayout(self.inputArea2.layout)
        self.tab2.layout.addWidget(self.inputArea2,3,1)

        self.input2 = QLineEdit()
        self.input2.setFixedWidth(250)
        self.input2.setFixedHeight(40)
        self.input2.returnPressed.connect(self.searchID)
        #self.input.setStyleSheet("height: 100px;")
        self.input2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input2.setStyleSheet("font-size: 25pt;")
        self.inputArea2.layout.addWidget(self.input2, 0, 1)
 
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.searchID)
        self.searchButton.setStyleSheet("font-size: 25pt;")
        self.inputArea2.layout.addWidget(self.searchButton, 1,1)
 
        self.clearButton2 = QPushButton("Clear")
        self.clearButton2.clicked.connect(self.input2.clear)
        self.clearButton2.clicked.connect(
            lambda: self.message2.setText("")
        )
        self.clearButton2.setStyleSheet("font-size: 25pt;")
        self.inputArea2.layout.addWidget(self.clearButton2, 2, 1)

        self.message2 = QLabel("")
        self.message2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message2.setStyleSheet("font-size: 25pt;")
        self.message2.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse);
        self.tab2.layout.addWidget(self.message2, 4, 1)

        #--------------------
        #Tab 3 Content
        #--------------------
##        self.tab3.layout = QVBoxLayout(self)
##        self.tab3.setLayout(self.tab3.layout)
##        self.tab3.setStyleSheet("background-color: #ffffff;")
##        
##        self.label2 = QLabel("Page Under Construction")
##        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
##        self.tab3.layout.addWidget(self.label2)

        self.tab3.layout = QGridLayout(self)
        self.tab3.setLayout(self.tab3.layout)
        self.tab3.setStyleSheet("background-color: #bad3fe;")#ffffff;")

        self.header3 = QLabel("Found a lost fob, but don't know whose it is?")
        self.header3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header3.setFont(headerFont)
        self.header3.setStyleSheet("font-size: 35pt;")
        self.tab3.layout.addWidget(self.header3, 1,1)

        self.instructions3 = QLabel("Scan the fob and find out who it belongs to!")
        self.instructions3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions3.setStyleSheet("font-size: 25pt;")
        self.tab3.layout.addWidget(self.instructions3, 2,1)

        self.inputArea3 = QWidget()
        self.inputArea3.layout = QGridLayout(self)
        self.inputArea3.setLayout(self.inputArea3.layout)
        self.tab3.layout.addWidget(self.inputArea3,3,1)

        self.input3 = QLineEdit()
        self.input3.setFixedWidth(250)
        self.input3.setFixedHeight(40)
        self.input3.setStyleSheet("font-size: 25pt;")
        self.input3.returnPressed.connect(self.identifyFob)
        self.input3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inputArea3.layout.addWidget(self.input3, 0, 1)
 
        self.searchButton3 = QPushButton("Search")
        self.searchButton3.clicked.connect(self.identifyFob)
        self.searchButton3.setStyleSheet("font-size: 25pt;")
        self.inputArea3.layout.addWidget(self.searchButton3, 1,1)
 
        self.clearButton3 = QPushButton("Clear")
        self.clearButton3.clicked.connect(self.input3.clear)
        self.clearButton3.setStyleSheet("font-size: 25pt;")
        self.inputArea3.layout.addWidget(self.clearButton3, 2, 1)

        self.message3 = QLabel("")
        self.message3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message3.setStyleSheet("font-size: 25pt;")
        self.tab3.layout.addWidget(self.message3, 4, 1)

        
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def login(self):
        ID = self.input.text()

        if (ID ==""):
            self.message.setText("")
            return None
        
        try:
            ID = int(ID)
        except:
            self.message.setText("Make sure the input is a number.")

        name = lookupName(ID)

        if (name != None):
           
##            self.thread = QThread()
##            
##            self.worker = Worker()
##            self.worker.moveToThread(self.thread)
##            self.thread.started.connect(#self.worker.run)
##                lambda: self.worker.logAttendance(SPREADSHEET_KEY, name, ID)
##            )
##            self.worker.progress.connect(print)#self.message.setText)
##            self.worker.finished.connect(self.thread.quit)
##            self.worker.finished.connect(self.worker.deleteLater)
##            self.thread.finished.connect(self.thread.deleteLater)
##            
##
##            self.thread.start()
##
##            self.thread.finished.connect(
##                lambda: self.message.setText(name + " is logged in.")
##            )
##
##            self.thread.finished.connect(self.input.clear)
            
            #print("logging in")
            #self.message.setText("Logging in...")
            self.message.update()
            logAttendance(SPREADSHEET_KEY, name, ID)
            self.input.clear()
            self.message.setText(name + " is logged in.")

        else:
            print("Error! ID number is not associated with a name.")
            self.message.setText("Error! Problem logging in.")
            self.input.clear()

    def searchID(self):
        #print("HI")
        name = self.input2.text()
        ID = lookupID(name)

        if (name ==""):
            self.message2.setText("")
            return None
        
        if (ID != None):

            print("Name: " + name)
            self.input2.clear()
            self.message2.setText("ID Number: " + str(ID))

        else:
            print("Error! ID number is not associated with a name.")
            self.message2.setText("Error! Name not found in database.")
            self.input2.clear()

    def identifyFob(self):
        ID = self.input3.text()

        if (ID ==""):
            self.message3.setText("")
            return None
        
        try:
            ID = int(ID)
        except:
            self.message3.setText("Make sure the input is a number.")

        name = lookupName(ID)

       
        if (name != None):
            
            self.input3.clear()
            self.message3.setText("Fob " + str(ID) + " belongs to " +name + ".")

        else:
            self.message3.setText("Error! ID number is not associated with a name.")
            self.input3.clear()
        
#-----------------------------------------------------------------------
# GOOGLE SPREADSHEET CODE
#-----------------------------------------------------------------------

##def lookupID(fname, lname):
##    pass
##

def lookupName(idNumber):
    #print(ids)
    for i in range(len(ids)):
        #print (ids[i])
        if (ids[i] == idNumber):
            return(firstNames[i] + " " + lastNames[i])

    return None

def lookupID(name):
    for i in range(len(firstNames)):
        if ((firstNames[i]+ " " + lastNames[i])==name):
            return(ids[i])

    return None


def updateIDData(SK):
    sh = gc.open_by_key(SK)

    wl = sh.worksheets()
    #print(wl)

    ds = wl[1]
    #print(ds)
    ln = ds.col_values(1)[1:]
    fn = ds.col_values(2)[1:]
    newIDs = ds.col_values(3)[1:]
    #print(newIDs)

    for i in range(len(newIDs)):
        newIDs[i] = int(newIDs[i])

    return ln, fn, newIDs


def logAttendance(SK, name, ID):
    sh = gc.open_by_key(SK)
    wl = sh.worksheets()
    date = dt.datetime.now()
    ds = wl[0]
    ds.append_row([date.strftime('%c'), ID, name, "General Meeting"])



#-----------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    gc = gspread.service_account(filename='credentials.json')

    lastNames, firstNames, ids = updateIDData(SPREADSHEET_KEY)
        

    #print(lookupName(3504000028))
    #print(lookupID("Rosie Riveter"))

    #attendanceSheet = worksheet_list[0]

    #date = dt.datetime.now()
    #attendanceSheet.append_row([date.strftime('%c'), "010203390", "Elizabeth Kysel", "General Meeting"])
    
    #print(date)
    sys.exit(app.exec())

   


    
