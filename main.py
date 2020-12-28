################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# GUI FILE
from ui_main import Ui_MainWindow
# IMPORT FUNCTIONS
from ui_functions import *

from random import shuffle
# from frmStart import *



class MainWindow(QMainWindow):
    # List lưu trữ 5 từ vựng mỗi Box
    lstPracticeBox1=[]
    lstPracticeBox2=[]
    lstPracticeBox3=[]
    lstPracticeBox4=[]
    lstPracticeBox5=[]
    
    def loadVocabulary(self):
        Date_Now = date.today()
        Date_Old = findMaxDate()

        print(Date_Now)
        print(Date_Old)
        if Date_Now > Date_Old:  
            #Cập nhật lại những từ trả lời đúng của ngày trước
            # Nếu trả lời đúng thì sẽ tăng thêm 1 level
            # Ví dụ từ ở Box1 trả lời đúng thì từ đó sẽ được đưa lên Box 2
            updateBox(Date_Old)
            lstBox1 = find_by_level_box(1)
            print(lstBox1)
            print("nghia")
            shuffle(lstBox1)
            lstPracticeBox1=lstBox1[0:5]
            ############################
            lstBox2 = find_by_level_box(2)
            shuffle(lstBox2)
            lstPracticeBox2=lstBox2[0:5]
            #############################
            lstBox3 = find_by_level_box(3)
            shuffle(lstBox3)
            lstPracticeBox3=lstBox3[0:5]
            #############################
            lstBox4 = find_by_level_box(4)
            shuffle(lstBox4)
            lstPracticeBox4=lstBox4[0:5]
            #############################
            lstBox5 = find_by_level_box(5)
            shuffle(lstBox5)
            lstPracticeBox5=lstBox5[0:5]
            #############################
            #insert vào mỗi Box 5 từ 
            for item in lstPracticeBox1:
                addReview(item[0])
            for item in lstPracticeBox2:
                addReview(item[0])
            for item in lstPracticeBox3:
                addReview(item[0])
            for item in lstPracticeBox4:
                addReview(item[0])
            for item in lstPracticeBox5:
                addReview(item[0])


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadVocabulary()
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # Box 1
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_2.clicked.connect(lambda:UIFunctions.mapping(self,1))
        # Box 2
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda:UIFunctions.mapping(self,2))
        # Box 3
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_4.clicked.connect(lambda:UIFunctions.mapping(self,3))
        # Box 4
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_5.clicked.connect(lambda:UIFunctions.mapping(self,4))
        # Box 5
        self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_6.clicked.connect(lambda:UIFunctions.mapping(self,5))
        # Box Custom
        self.ui.btnCustom.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnCustom.clicked.connect(lambda:UIFunctions.mapping(self,0))
        # Box Recruitment
        self.ui.btnRecruitment.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnRecruitment.clicked.connect(lambda:UIFunctions.mapping(self,0))
        # Box Workplace
        self.ui.btnWorkplace.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnWorkplace.clicked.connect(lambda:UIFunctions.mapping(self,0))
        # Box Bussiness
        self.ui.btnBussiness.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnBussiness.clicked.connect(lambda:UIFunctions.mapping(self,0))
        # Box Shopping
        self.ui.btnShopping.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnShopping.clicked.connect(lambda:UIFunctions.mapping(self,0))
        # Box Travel
        self.ui.btnTravel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnTravel.clicked.connect(lambda:UIFunctions.mapping(self,0))

        #Edit
        self.ui.btn_edit.clicked.connect(lambda:UIFunctions.edit_Vocabulary(self.ui))
        #Delete
        self.ui.btn_delete.clicked.connect(lambda:UIFunctions.delete_Vocabulary(self))
        #Practice
        self.ui.btn_practice.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frmPractice))
        self.ui.btn_practice.clicked.connect(lambda: UIFunctions.findListPractice(self))
        #Submit
        self.ui.btnSubmit.clicked.connect(lambda: UIFunctions.isCorrect(self,self.ui.lstPractice[0][1]))
        #Micro
        self.ui.btnMic.clicked.connect(lambda: UIFunctions.listenning(self))
        #Review 
        self.ui.btn_review.clicked.connect(lambda: UIFunctions.reviewVocabulary(self))
        #Cancel ở form Practice
        self.ui.btnCancel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnCancel.clicked.connect(lambda:UIFunctions.mapping(self,self.ui.level))
        #Đọc từ vựng ở trong ô text
        self.ui.btnSpeak.clicked.connect(lambda: UIFunctions.speaking(self))

        #self.ui.Btn_Toggle.clicked.connect(lambda:UIFunctions.hideButton(self))
        #self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Form = QtWidgets.QWidget()
    # ui = Ui_Form()
    # ui.setupUi(Form)
    # Form.show()
    window = MainWindow()
    sys.exit(app.exec_())

