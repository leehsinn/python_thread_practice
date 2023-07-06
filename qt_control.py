from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep
import threading

'''def do_something():
    for time in range(10):
        ui.label.setText(str(time+1))
        #ui.progressBar.setValue(time*10) qt複雜的東西沒有辦法使用一般的thread
        sleep(1)
        ui.label.setText("end")

def click_button():
    t = threading.Thread(target = do_something)
    t.start()'''

global number
number = 0


def timer_count():
    global number
    ui.label.setText(str(number))
    ui.progressBar.setValue(number*10)
    number+=1
    '''if number == 10:
        timer.stop()
        number = 0'''


def click_button():
    global number
    print(ui.label.text())

    if number != 0: 
        ui.label.setText(str(0))
        number = 0
        ui.pushButton.setText("start")
    else:
        timer.start(1000)
        ui.pushButton.setText("clear")

def pause_count():
    timer.stop()

def clear_count():
    ui.label.setText(str(0))
    number = 0

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

timer = QTimer()
timer.timeout.connect(timer_count)
ui.pushButton.clicked.connect(click_button)
ui.clearButton.clicked.connect(clear_count)
ui.pauseButton.clicked.connect(pause_count)

widget.show()
app.exec_()