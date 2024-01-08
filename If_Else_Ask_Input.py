#Assignment 4

#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

#PsuedoCode
#Set up GUI
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox)
from PyQt5.QtGui import QFont, QColor, QPainter, QPalette
from PyQt5.QtCore import Qt

#Set up widgets
class LargestNumberFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #window size and title
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Find the Largest Number')

        #layout
        layout = QVBoxLayout()

        #font
        font = QFont('Arial', 12)

        #style widgets
        self.label1 = QLabel('Enter First Number:')
        self.label1.setFont(font)
        layout.addWidget(self.label1)

        self.entry1 = QLineEdit()
        self.entry1.setFont(font)
        layout.addWidget(self.entry1)

        self.label2 = QLabel('Enter Second Number:')
        self.label2.setFont(font)
        layout.addWidget(self.label2)

        self.entry2 = QLineEdit()
        self.entry2.setFont(font)
        layout.addWidget(self.entry2)

        self.label3 = QLabel('Enter Third Number:')
        self.label3.setFont(font)
        layout.addWidget(self.label3)

        self.entry3 = QLineEdit()
        self.entry3.setFont(font)
        layout.addWidget(self.entry3)

        self.findButton = QPushButton('Find Largest Number')
        self.findButton.setFont(font)
        self.findButton.clicked.connect(self.showLargest)
        layout.addWidget(self.findButton)

        self.setLayout(layout)

        #background color
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(240, 240, 240))
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #main window
        self.show()

    
    
    #Ask the user to input 3 numbers
    def showLargest(self):
        try:
            #Ask to input number 1
            num1 = float(self.entry1.text())

            #Ask to input number 2
            num2 = float(self.entry2.text())
            #Ask to input number 3
            num3 = float(self.entry3.text())

            #Check if the input are numbers
            if num1 >= num2 and num1 >= num3:
                largest = num1
            elif num2 >= num3:
                largest = num2
            else:
                largest = num3

            #If the input are numbers find and print the biggest number
            QMessageBox.information(self, 'Result', f'The largest number is: {largest}')
        
        #If the input is not a number print "please input a number"
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please input a number.')

def main():
    app = QApplication(sys.argv)
    ex = LargestNumberFinder()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()

