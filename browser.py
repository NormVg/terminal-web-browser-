from PyQt5.QtWidgets  import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

url = open("./link.txt","rt")
link = url.read()
url.close()
#print(link)


delete_time = open("./link.txt",'r+')
delete_time.truncate(0)
delete_time.close()
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(link))
        self.setCentralWidget(self.browser)
        self.showNormal()
        #https://thenorm.netlify.app
app = QApplication(sys.argv)
QApplication.setApplicationName("<B-R-O-W-S-E-R>")
window = MainWindow()
app.exec_()