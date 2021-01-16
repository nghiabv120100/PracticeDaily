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
from PyQt5 import QtCore, QtGui, QtWidgets

numwords=0

class MainWindow(QMainWindow):
    # List lưu trữ 5 từ vựng mỗi Box
    lstPracticeBox1=[]
    lstPracticeBox2=[]
    lstPracticeBox3=[]
    lstPracticeBox4=[]
    lstPracticeBox5=[]
    
    def loadVocabulary(self):
        global numwords
        Date_Now = date.today()
        Date_Old = findMaxDate()
        length=numwords
        print("Num",numwords)
        print(Date_Now)
        print(Date_Old)
        if Date_Now > Date_Old:  
            #Cập nhật lại những từ trả lời đúng của ngày trước
            # Nếu trả lời đúng thì sẽ tăng thêm 1 level
            # Ví dụ từ ở Box1 trả lời đúng thì từ đó sẽ được đưa lên Box 2
            updateBox(Date_Old)
            lstBox1 = find_by_level_box(1)
            print(lstBox1)
          
            shuffle(lstBox1)
            if len(lstBox1) > 30: 
                length=numwords+len(lstBox1)//10
            lstPracticeBox1=lstBox1[0:length]
            ############################
            lstBox2 = find_by_level_box(2)
            shuffle(lstBox2)
            if len(lstBox2) > 30: 
                length=numwords+len(lstBox1)//10           
            lstPracticeBox2=lstBox2[0:length]
            #############################
            lstBox3 = find_by_level_box(3)
            shuffle(lstBox3)
            if len(lstBox3) > 30: 
                length=numwords+len(lstBox1)//10
            lstPracticeBox3=lstBox3[0:length]
            #############################
            lstBox4 = find_by_level_box(4)
            shuffle(lstBox4)
            if len(lstBox4) > 30: 
                length=numwords+len(lstBox1)//10
            lstPracticeBox4=lstBox4[0:length]
            #############################
            lstBox5 = find_by_level_box(5)
            shuffle(lstBox5)
            if len(lstBox5) > 30: 
                length=numwords+len(lstBox1)//10
            lstPracticeBox5=lstBox5[0:length]
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
        #Box Source
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_1.clicked.connect(lambda:UIFunctions.assignLevel(self,0))
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
        # Box Done
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_7.clicked.connect(lambda:UIFunctions.mapping(self,6))
        # Box Custom
        self.ui.btnCustom.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnCustom.clicked.connect(lambda:UIFunctions.mapping(self,-1))
        # Box Recruitment
        self.ui.btnRecruitment.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnRecruitment.clicked.connect(lambda:UIFunctions.mapping(self,-2))
        # Box Workplace
        self.ui.btnWorkplace.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnWorkplace.clicked.connect(lambda:UIFunctions.mapping(self,-3))
        # Box Bussiness
        self.ui.btnBussiness.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnBussiness.clicked.connect(lambda:UIFunctions.mapping(self,-4))
        # Box Shopping
        self.ui.btnShopping.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnShopping.clicked.connect(lambda:UIFunctions.mapping(self,-5))
        # Box Travel
        self.ui.btnTravel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btnTravel.clicked.connect(lambda:UIFunctions.mapping(self,-6))

        #Edit or Save
        self.ui.btn_edit.clicked.connect(lambda:UIFunctions.edit_Vocabulary(self))
        #Delete
        self.ui.btn_delete.clicked.connect(lambda:UIFunctions.delete_Vocabulary(self))
        #Practice
        #self.ui.btn_practice.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frmPractice))
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

        #Quit để thoát ứng dụng
        
        self.ui.btnQuit.clicked.connect( lambda:UIFunctions.message_box(self))

        #Result để xem biểu đồ thống kê kết quả học tập
        self.ui.btnResult.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btnResult.clicked.connect(lambda:UIFunctions.assignLevel(self,7))
        # self.ui.btnResult.clicked.connect( lambda:drawGraph())
        # Xem thống kê tình hình học tập từ ngày A đến ngày B
        self.ui.btnShowResultByDay.clicked.connect(lambda: drawGraph(self.ui.dateFrom.date(),self.ui.dateTo.date()))
        # Xem thống kê tình hình học tập trong tháng
        self.ui.btnShowResultByMonth.clicked.connect(lambda: drawGraph(self.ui.dateMonth.date(),QDate(self.ui.dateMonth.date().year(),self.ui.dateMonth.date().month(),numberOfDays(self.ui.dateMonth.date().year(),self.ui.dateMonth.date().month()))))
        # Xuất ra excel tình hình học tập từ ngày A đến ngày B
        self.ui.btnExportResultByDay.clicked.connect(lambda: exportToExcel(self.ui.dateFrom.date(),self.ui.dateTo.date()))
        # Xem thống kê tình hình học tập trong tháng
        self.ui.btnExportResultByMonth.clicked.connect(lambda: exportToExcel(self.ui.dateMonth.date(),QDate(self.ui.dateMonth.date().year(),self.ui.dateMonth.date().month(),numberOfDays(self.ui.dateMonth.date().year(),self.ui.dateMonth.date().month()))))
       
        
        # Khi nhấn vào table vocabylary thì sẽ binding dữ liệu sang form
        self.ui.tlwBoxWord.clicked.connect(lambda:UIFunctions.displayDetailVocabulary(self))
        # Khi nhấn vào button chọn hình ảnh
        self.ui.btn_image.clicked.connect(lambda:UIFunctions.loadImage(self))
        # Khi nhấn vào nút Cancel để huỷ thao tác Edit hoặc Add từ vựng
        self.ui.btn_cancel.clicked.connect(lambda:UIFunctions.cancelEditOrAdd(self))
        # Đổi tên Box theo số từ còn lại ở trong Box
        for i in range(1,6):
            UIFunctions.renameBox(self,i)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        
        self.show()
        ## ==> END ##
class Ui_Form(object):
        def setupUi(self, Form):
            
                def easyLevel():
                        print(1)
                        global numwords
                        numwords = 3
                        Form.setHidden(True)
                        MainWindow()
                def mediumLevel():
                        global numwords
                        print(2)
                        numwords = 5
                        Form.setHidden(True)
                        MainWindow()
                def hardLevel():
                        print(3)
                        global numwords
                        numwords = 10
                        Form.setHidden(True)
                        MainWindow()
                Form.setObjectName("Form")
                Form.resize(403, 505)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
                Form.setSizePolicy(sizePolicy)
                Form.setAutoFillBackground(False)
                Form.setStyleSheet("background:rgb(2, 14, 30) ")
                self.btnEasy = QtWidgets.QPushButton(Form)
                self.btnEasy.setGeometry(QtCore.QRect(20, 20, 361, 131))
                self.btnEasy.clicked.connect(easyLevel)
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.btnEasy.setFont(font)
                self.btnEasy.setStyleSheet("background:rgb(85, 170, 255);\n"
        "color:rgb(255, 255, 255)")
                self.btnEasy.setObjectName("btnEasy")
                self.btnMedium = QtWidgets.QPushButton(Form)
                self.btnMedium.setGeometry(QtCore.QRect(20, 160, 361, 131))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.btnMedium.setFont(font)
                self.btnMedium.setStyleSheet("background:rgb(85, 170, 255);\n"
        "color:rgb(255, 255, 255)")
                self.btnMedium.setObjectName("btnMedium")
                self.btnHard = QtWidgets.QPushButton(Form)
                self.btnMedium.clicked.connect(mediumLevel)
                self.btnHard.setGeometry(QtCore.QRect(20, 300, 361, 131))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.btnHard.setFont(font)
                self.btnHard.setStyleSheet("background:rgb(85, 170, 255);\n"
        "color:rgb(255, 255, 255)")
                self.btnHard.setObjectName("btnHard")
                self.label = QtWidgets.QLabel(Form)
                self.btnHard.clicked.connect(hardLevel)
                self.label.setGeometry(QtCore.QRect(30, 450, 341, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
                self.label.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setStyleSheet("color:rgb(255, 255, 255)")
                self.label.setObjectName("label")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)
                
        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.btnEasy.setText(_translate("Form", "Easy"))
                self.btnMedium.setText(_translate("Form", "Medium"))
                self.btnHard.setText(_translate("Form", "Hard"))
                self.label.setText(_translate("Form", "Vui lòng chọn độ khó để tiếp tục."))

if __name__ == "__main__":
        Date_Now = date.today()
        Date_Old = findMaxDate()
        app = QApplication(sys.argv)

        print(Date_Now)
        print(Date_Old)
        if Date_Now > Date_Old:
                Form = QtWidgets.QWidget()
                ui = Ui_Form()
                ui.setupUi(Form)
                Form.show()
        else:
                MainWindow()
        sys.exit(app.exec_())   
         
