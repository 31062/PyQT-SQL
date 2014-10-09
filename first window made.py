import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class window (QMainWindow):
    """a simple blank window"""

    #constructor
    def __init__(self):
        super().__init__()# calls super class
        self.setWindowTitle("window")
        #create QActions
        self.open_database = QAction("open database",self)
        self.close_database = QAction("close datanase",self)
        #create menu and tool bars
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()
        #add to menubar
        self.database_menu = self.menu.address("database")
        #add actions to menu
        self.database_menu.addAction(self,open_database)
        self.database_menu.addAction(self,close_database)
        #add action to toolbar
        self.database_toolbar.addAction(self.open_database)
        #connection
        self.open_database.triggerd.connect(self.open_database)
        #files
        path = QFileDielog.getOpenFileName()
        

    def main():
        app = QApplication(sys.argv)#creates a new applicaton
        window = window() # creates a new instance
        window.show() #makes window visable
        window.raise_() #RAISE WINDOW TO TOP OF WINDOW STACK
        app.exec_()
        
