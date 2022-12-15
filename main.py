from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup, QHBoxLayout, QWidget
from PyQt5.QtCore import QMutex, QWaitCondition
import pickle
import text
import char
import location

from gui import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)

        self.textBrowser_2.setText("HP: 100/"+ str(char.stats["vit"] * 10) + " Mana: 100/100\n"
        "Stamina 100/100\n"
        "End: " + str(char.stats["end"]) + " Vit: " + str(char.stats["vit"]) +
        "\nDex: " + str(char.stats["dex"]) + " Agl: " + str(char.stats["dex"]) +
        "\nPer: " + str(char.stats["per"]) + " Cha: " + str(char.stats["cha"]) +
        "\nInt: " + str(char.stats["int"]) + " Wis: " + str(char.stats["wis"]) +
        "\nStr: " + str(char.stats["str"]) + " age: "+ str(char.stats["age"]) +
        "\nTime: 0/20 weeks")
        
        self.Button_1.clicked.connect(self.on_click)
        self.Button_2.clicked.connect(self.on_click)
        self.Button_3.clicked.connect(self.on_click)
        self.Button_4.clicked.connect(self.on_click)
        self.Button_5.clicked.connect(self.on_click)
        self.Button_6.clicked.connect(self.on_click)
        self.Button_7.clicked.connect(self.on_click)
        self.Button_8.clicked.connect(self.on_click)

        
        self.player = 'house_1'
        self.test()
    @QtCore.pyqtSlot()
    def on_click(self) -> None:
        object_sender = self.sender()
        if object_sender.objectName() == "Button_1":
            self.key = 1
        if object_sender.objectName() == "Button_2":
            self.key = 2
        if object_sender.objectName() == "Button_3":
            self.key = 3
        if object_sender.objectName() == "Button_4":
            self.key = 4
        if object_sender.objectName() == "Button_5":
            self.key = 5
        if object_sender.objectName() == "Button_6":
            self.key = 6
        if object_sender.objectName() == "Button_7":
            self.key = 7
        if object_sender.objectName() == "Button_8":
            self.key = 8
        self.test()
    def test(self):
        self.i = 0
        for self.i in range(8):
            if self.i == 1:
                self.Button_1.setText('')
            if self.i == 2:
                self.Button_2.setText('')
            if self.i == 3:
                self.Button_3.setText('')
            if self.i == 4:
                self.Button_4.setText('')
            if self.i == 5:
                self.Button_5.setText('')
            if self.i == 6:
                self.Button_6.setText('')
            if self.i == 7:
                self.Button_7.setText('')
            if self.i == 8:
                self.Button_8.setText('')
        self.i = 1
        while self.i < len(location.locations[self.player][1]):
            if self.i == 1 and location.locations[self.player][1][x][1] != False:
                self.Button_1.setText(location.locations[self.player][1][x][0])
            if self.i == 2 and location.locations[self.player][1][x][1] != False:
                self.Button_2.setText(location.locations[self.player][1][x][0])
            if self.i == 3 and location.locations[self.player][1][x][1] != False:
                self.Button_3.setText(location.locations[self.player][1][x][0])
            if self.i == 4 and location.locations[self.player][1][x][1] != False:
                self.Button_4.setText(location.locations[self.player][1][x][0])
            if self.i == 5 and location.locations[self.player][1][x][1] != False:
                self.Button_5.setText(location.locations[self.player][1][x][0])
            if self.i == 6 and location.locations[self.player][1][x][1] != False:
                self.Button_6.setText(location.locations[self.player][1][x][0])
            if self.i == 7 and location.locations[self.player][1][x][1] != False:
                self.Button_7.setText(location.locations[self.player][1][x][0])
            if self.i == 8 and location.locations[self.player][1][x][1] != False:
                self.Button_8.setText(location.locations[self.player][1][x][0])
            self.i = self.i + 1
        for x in range(len(location.locations[self.player][2][1])):
            if self.i == 1:
                self.Button_1.setText(location.locations[self.player][2][1][x])
            if self.i == 2:
                self.Button_2.setText(location.locations[self.player][2][1][x])
            if self.i == 3:
                self.Button_3.setText(location.locations[self.player][2][1][x])
            if self.i == 4:
                self.Button_4.setText(location.locations[self.player][2][1][x])
            if self.i == 5:
                self.Button_5.setText(location.locations[self.player][2][1][x])
            if self.i == 6:
                self.Button_6.setText(location.locations[self.player][2][1][x])
            if self.i == 7:
                self.Button_7.setText(location.locations[self.player][2][1][x])
            if self.i == 8:
                self.Button_8.setText(location.locations[self.player][2][1][x])
        self.textBrowser_4.setText(location.locations[self.player][2][0])
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyApp()
    ui.show()
    sys.exit(app.exec_())
