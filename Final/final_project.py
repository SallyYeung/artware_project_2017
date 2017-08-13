"""
Artware Project:
Project inspired from the adware and malware from free software(Tecent manager).
The images of advertisement are generated randomly
For more detail description and research, please visit the wordpress:


Reference:
Inclass example by Jonathan

PyQt5 widgets II:
http://zetcode.com/gui/pyqt5/widgets2/


"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QUrl, QRect, Qt, QSize
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtMultimedia import QSound
from random import randint
import random
import sys


#Make the bottom-left malware
class MalwareWindow(QWidget):
    def __init__(self, xpos, ypos, title):
        super(MalwareWindow, self).__init__()
        self.acceleration = 5.0
        self.velocity = 0.0
        self.xvel = 0.0
        self.screenHeight = qApp.desktop().availableGeometry().height() # height of the screen
        self.screenWidth = qApp.desktop().availableGeometry().width() # height of the screen

        self.sound = QSound("sounds/test.wav")
        self.makeotherWin(xpos, ypos, title)
        self.initUI()

    def makeotherWin(self, xpos, ypos, title):
        self.setGeometry(xpos, ypos, 200, 100)
        self.setWindowTitle(title)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animateFrame)
        self.timer.start(1000 / 12) # 12 frames per second

    # this function gets called 12 times per second
    def animateFrame(self):
        xpos = self.pos().x() + self.xvel
        ypos = self.pos().y() + self.velocity # move the ypos a little bit

        if (xpos + self.width()) > self.screenWidth and (ypos + self.height()) > self.screenHeight:
            xpos = self.screenWidth - self.width()
            if abs(self.xvel) <= self.acceleration:
                self.xvel = 0.0
            else:
                self.sound.play()
                self.xvel *= -0.5

        if (ypos + self.height()) > self.screenHeight:
            ypos = self.screenHeight - self.height()
            if abs(self.velocity) <= self.acceleration:  # when the velocity is very small, just set it to 0.0 to keep from infinite bouncing
                self.velocity = 0.0
            else:
                self.sound.play()
                self.velocity *= -0.5 # velocity of movement changes direction
        self.move(xpos, ypos)
        self.velocity += self.acceleration
        self.xvel += self.acceleration

## insert image as widget
    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("warning.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setWindowTitle('Red Rock')
        self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

##########################
#Bouncing advertisement
class Gif_win(QWidget):



    def __init__(self, xpos, ypos, title):
        super(Gif_win, self).__init__()
        self.screenHeight = qApp.desktop().availableGeometry().height() # height of the screen
        self.screenWidth = qApp.desktop().availableGeometry().width() # height of the screen

        self.sound = QSound("sounds/test.wav")
        self.makeotherWin(xpos, ypos, title)
        self.initUI()
        self.move(100, 200)

    def makeotherWin(self, xpos, ypos, title):
        self.setGeometry(xpos, ypos, 200, 100)
        self.xacceleration = 5.0
        self.yacceleration = 5.0
        self.back1 = 1.0
        self.back2 = 1.0


        self.setWindowTitle(title)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animateFrame)
        self.timer.start(1000 / 12) # 12 frames per second

    # this function gets called 12 times per second
    def animateFrame(self):


        xpos = self.pos().x()
        ypos = self.pos().y()


        if (xpos + self.width()) < self.screenWidth and (ypos + self.height()) < self.screenHeight:

            xpos = self.pos().x() + self.xacceleration
            ypos = self.pos().y() + self.yacceleration
        else :
            self.xacceleration *= -1
            self.yacceleration *= -1
            xpos = self.pos().x() - 5
            ypos = self.pos().y() - 5
            self.sound.play()

        if xpos == 0 or ypos == 0:
            xpos = self.pos().x() + 5
            ypos = self.pos().y() + 5
            self.xacceleration *= -1
            self.yacceleration *= -1
            self.sound.play()

        self.move(xpos, ypos)



    def initUI(self):

        okButton = QPushButton("OK")
        cancel = QPushButton("cancel")
        hbox = QHBoxLayout(self)
        #Generate random img
        m = randint(1,3)
        if m == 1:
            n = "gift.png"
        if m == 2:
            n = "iphone.png"
        if m == 3:
            n = "help.png"

        pixmap = QPixmap(n)
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        hbox.addWidget(okButton)
        hbox.addWidget(cancel)
        okButton.clicked.connect(self.download)
        cancel.clicked.connect(self.link)

        self.setLayout(hbox)


        self.setWindowTitle('Red Rock')
        self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

    def download(self):
        print 'Downloading Package ...'

    def link(self):
        print 'Transfering you information...'

########################
class Software(QWidget):

    def __init__(self):
        super(Software, self).__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("antivirus.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setWindowTitle('Red Rock')
        self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

#########################
class Button(QWidget):
    buttonStyle = """
        QPushButton {
            font-size: 22px;
            font-weight: bold;
            background-color: red;
            border-radius: 50px;
            border: 6px dashed lightgrey;
            max-width: 110px;
            max-height: 95px;
        }
        QPushButton:checked {
            background-color: #d9ffb3;
        }
    """

    def __init__(self):
        super(Button, self).__init__()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True) # give the timer one-shot behavior
        self.timer.timeout.connect(self.unclick) #connect timeout to our unclick method
        self.makeWindow()
        self.move(548, 420)



    def makeWindow(self):
        self.but = QPushButton("Clear Ads", self)
        self.but.setGeometry(self.rect())
        self.but.setCheckable(True) # make this button behave like a checkbox
        self.but.clicked.connect(self.turnOn)
        self.but.setStyleSheet(self.buttonStyle)
        self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        self.setAttribute(Qt.WA_TranslucentBackground)


        self.show()


    def turnOn(self):
        self.but.setText("Checking")
        self.timer.start(4000)

    def unclick(self):
        self.but.setText("No Result")
        self.but.setChecked(False)

##########################



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Software()
    mywin = Button()
    test1 = MalwareWindow(randint(50,300), randint(50,300), "MalWin")
    gift1 = Gif_win(random.randrange(50,300,5), random.randrange(50,300,5), "ad1")
    gift2 = Gif_win(random.randrange(300,800,5), random.randrange(5,400,5), "ad2")
    gift3 = Gif_win(random.randrange(300,800,5), random.randrange(5,400,5), "ad3")
    #show the function
    test1.show()
    gift1.show()
    gift2.show()
    gift3.show()
    sys.exit(app.exec_())
