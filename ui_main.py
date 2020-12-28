# -*- coding: utf-8 -*-

################################################################################
## self.frmPractice generated from reading UI file 'ui_mainrvpJdh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

    level =0
    lstPractice =[]
    lstCorrect=[]
    lstWrong=[]
    voice ="..."  # lưu speech to text

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        


        self.horizontalLayout.addWidget(self.frame_toggle)

        #Tạo button Edit
        self.btn_edit = QPushButton(self.frame_toggle)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMinimumSize(QSize(0, 40))
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_edit)
        #Tạo button Delete
        self.btn_delete = QPushButton(self.frame_toggle)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(0, 40))
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_delete)
        #Tạo button Practice
        self.btn_practice = QPushButton(self.frame_toggle)
        self.btn_practice.setObjectName(u"btn_practice")
        self.btn_practice.setMinimumSize(QSize(0, 40))
        self.btn_practice.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_practice)
        #Tạo button review
        self.btn_review = QPushButton(self.frame_toggle)
        self.btn_review.setObjectName(u"btn_review")
        self.btn_review.setMinimumSize(QSize(0, 40))
        self.btn_review.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_review)
        #Tạo button Cancel
        self.btnQuit = QPushButton(self.frame_toggle)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setMinimumSize(QSize(0, 40))
        self.btnQuit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btnQuit)
        
        ##############

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        #Taoj button page 1
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)

        #Tạo button page_4

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.verticalLayout_4.addWidget(self.btn_page_4)
        #Tạo button page_5
        
        self.btn_page_5 = QPushButton(self.frame_top_menus)
        self.btn_page_5.setObjectName(u"btn_page_5")
        self.btn_page_5.setMinimumSize(QSize(0, 40))
        self.btn_page_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_5)

       

        #Tạo button page_6


        self.btn_page_6 = QPushButton(self.frame_top_menus)
        self.btn_page_6.setObjectName(u"btn_page_6")
        self.btn_page_6.setMinimumSize(QSize(0, 40))
        self.btn_page_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_6)
        #Tạo button page_7

        self.btn_page_7 = QPushButton(self.frame_top_menus)
        self.btn_page_7.setObjectName(u"btn_page_7")
        self.btn_page_7.setMinimumSize(QSize(0, 40))
        self.btn_page_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_7)
        



        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(40)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"color: #FFF;")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        #Tạo table hiển thị từ vựng
        self.createTable(MainWindow)
        
        QMetaObject.connectSlotsByName(MainWindow)

        #Tạo form Practice
        self.frmPractice = QWidget()
        self.frmPractice.setObjectName(u"frmPractice")
        self.lblPicture = QtWidgets.QLabel(self.frmPractice)
        self.lblPicture.setGeometry(QtCore.QRect(270, 0, 221, 171))
        self.lblPicture.setObjectName("lblPicture")
        self.label = QtWidgets.QLabel(self.frmPractice)
        self.label.setGeometry(QtCore.QRect(200, 190, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: rgb(255,255,255);")
        self.txtMeans = QtWidgets.QTextEdit(self.frmPractice)
        self.txtMeans.setGeometry(QtCore.QRect(320, 190, 201, 41))
        self.txtMeans.setObjectName("txtMeans")
        self.txtMeans.setFont(font)
        self.txtMeans.setStyleSheet("color: rgb(255,255,255);")

        self.txtVocabulary = QtWidgets.QTextEdit(self.frmPractice)
        self.txtVocabulary.setGeometry(QtCore.QRect(320, 250, 201, 41))
        self.txtVocabulary.setObjectName("txtVocabulary")
        self.txtVocabulary.setFont(font)
        self.txtVocabulary.setStyleSheet("color: rgb(255,255,255);")
        self.label_2 = QtWidgets.QLabel(self.frmPractice)
        self.label_2.setGeometry(QtCore.QRect(150, 240, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: rgb(255,255,255);")
        self.btnMic = QtWidgets.QPushButton(self.frmPractice)
        self.btnMic.setGeometry(QtCore.QRect(270, 300, 51, 41))
        self.btnMic.setObjectName("btnMic")
        self.btnMic.setStyleSheet("color: rgb(255,255,255);")
        self.btnSpeak = QtWidgets.QPushButton(self.frmPractice)
        self.btnSpeak.setGeometry(QtCore.QRect(390, 300, 51, 41))
        self.btnSpeak.setObjectName("btnSpeak")
        self.btnSpeak.setStyleSheet("color: rgb(255,255,255);")
        self.btnSubmit = QtWidgets.QPushButton(self.frmPractice)
        self.btnSubmit.setGeometry(QtCore.QRect(240, 380, 101, 41))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.setStyleSheet("color: rgb(255,255,255);")
        self.btnCancel = QtWidgets.QPushButton(self.frmPractice)
        self.btnCancel.setGeometry(QtCore.QRect(390, 380, 111, 41))

        font = QtGui.QFont()
        font.setPointSize(14)
        
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.setStyleSheet("color: rgb(255,255,255);")
        self.stackedWidget.addWidget(self.frmPractice)
        self.lblPicture.setText(QCoreApplication.translate("MainWindow", "This is picture"))
        self.label.setText(QCoreApplication.translate("MainWindow", "Means:"))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Vocabulary:"))
        self.btnMic.setText(QCoreApplication.translate("MainWindow", "Mic"))
        self.btnSpeak.setText(QCoreApplication.translate("MainWindow", "Speak"))
        self.btnSubmit.setText(QCoreApplication.translate("MainWindow", "Submit"))
        self.btnCancel.setText(QCoreApplication.translate("MainWindow", "Cancel"))
        
        #Tạo form source
        self.btnCustom = QtWidgets.QPushButton(self.page_1)
        self.btnCustom.setGeometry(QtCore.QRect(50, 100, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustom.setFont(font)
        self.btnCustom.setStyleSheet("color:rgb(255, 255, 255) ;\n"
"background:rgb(85, 0, 255)")
        self.btnCustom.setObjectName("btnCustom")
        self.btnRecruitment = QtWidgets.QPushButton(self.page_1)
        self.btnRecruitment.setGeometry(QtCore.QRect(320, 100, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnRecruitment.setFont(font)
        self.btnRecruitment.setStyleSheet("color:rgb(255, 255, 255) ;\n"
"background:rgb(85, 0, 255)")
        self.btnRecruitment.setObjectName("btnRecruitment")
        self.btnWorkplace = QtWidgets.QPushButton(self.page_1)
        self.btnWorkplace.setGeometry(QtCore.QRect(570, 100, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnWorkplace.setFont(font)
        self.btnWorkplace.setStyleSheet("color:rgb(255, 255, 255) ;\n"
"background:rgb(85, 0, 255)")
        self.btnWorkplace.setObjectName("btnWorkplace")
        self.btnTravel = QtWidgets.QPushButton(self.page_1)
        self.btnTravel.setGeometry(QtCore.QRect(570, 250, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnTravel.setFont(font)
        self.btnTravel.setStyleSheet("color:rgb(255, 255, 255) ;\n"
"background:rgb(85, 0, 255)")
        self.btnTravel.setObjectName("btnTravel")
        self.btnShopping = QtWidgets.QPushButton(self.page_1)
        self.btnShopping.setGeometry(QtCore.QRect(320, 250, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnShopping.setFont(font)
        self.btnShopping.setStyleSheet("color:rgb(255, 255, 255) ;\n"
"background:rgb(85, 0, 255)")
        self.btnShopping.setObjectName("btnShopping")
        self.btnBussiness = QtWidgets.QPushButton(self.page_1)
        self.btnBussiness.setGeometry(QtCore.QRect(50, 250, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnBussiness.setFont(font)
        self.btnBussiness.setStyleSheet("color:rgb(255, 255, 255) ;\n"
"background:rgb(85, 0, 255)")
        self.btnBussiness.setObjectName("btnBussiness")

        self.retranslateUi(self.page_1)
        QtCore.QMetaObject.connectSlotsByName(self.page_1)

        self.btnCustom.setText(QCoreApplication.translate("Form", "Custom"))
        self.btnRecruitment.setText(QCoreApplication.translate("Form", "Recruitment"))
        self.btnWorkplace.setText(QCoreApplication.translate("Form", "Workplace"))
        self.btnTravel.setText(QCoreApplication.translate("Form", "Travel"))
        self.btnShopping.setText(QCoreApplication.translate("Form", "Shopping"))
        self.btnBussiness.setText(QCoreApplication.translate("Form", "Bussiness"))

        # setupUi

    def createTable(self,MainWindow):
         #################################################################
        #QTableWidget
        self.tlwBoxWord = QtWidgets.QTableWidget(self.page_2)
        self.tlwBoxWord.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.tlwBoxWord.setStyleSheet("Background-color:\"white\"")
        self.tlwBoxWord.setObjectName("tlwBoxWord")


        self.tlwBoxWord.setColumnCount(3)
        self.tlwBoxWord.setRowCount(1)
        self.tlwBoxWord.setItem(0,0, QTableWidgetItem("Vocabulary")) 
        self.tlwBoxWord.setItem(0,1, QTableWidgetItem("Part Of Speech"))
        self.tlwBoxWord.setItem(0,2, QTableWidgetItem("Means"))
        self.tlwBoxWord.horizontalHeader().setVisible(False)
        self.tlwBoxWord.verticalHeader().setVisible(False)

        #################################################################

    
            


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Box 1", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Box 2", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Box 3", None))
        self.btn_page_5.setText(QCoreApplication.translate("MainWindow", u"Box 4", None))
        self.btn_page_6.setText(QCoreApplication.translate("MainWindow", u"Box 5", None))
        self.btn_page_7.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_practice.setText(QCoreApplication.translate("MainWindow", u"Practice", None))
        self.btn_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        # self.label_1.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        # self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        #self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))

    # retranslateUi

