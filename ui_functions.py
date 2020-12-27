################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *
from LayerDAO import *
from Model import Word
import speech_recognition
import pyttsx3
from spellchecker import SpellChecker
spell = SpellChecker()
def showdialog(mess):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        msg.setText(mess)
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Notification")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
class UIFunctions(MainWindow):
    #Hiển thị thông báo
    
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def mapping(self,level):
        
        self.ui.level=level
        self.ui.lstWord=find_by_level_box(level) 
        if self.ui.level <=0:
            self.ui.btn_review.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        else:
            self.ui.btn_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))   
                   
        if len(self.ui.lstWord)==0:
            self.ui.tlwBoxWord.setColumnCount(3)
            self.ui.tlwBoxWord.setRowCount(1)
            self.ui.tlwBoxWord.setItem(0,0, QTableWidgetItem("Vocabulary")) 
            self.ui.tlwBoxWord.setItem(0,1, QTableWidgetItem("Part Of Speech"))
            self.ui.tlwBoxWord.setItem(0,2, QTableWidgetItem("Means"))


        i=1
        for row in self.ui.lstWord:
            self.ui.tlwBoxWord.setRowCount(i+1)
            self.ui.tlwBoxWord.setItem(i,0,QTableWidgetItem(row[1]))      
            self.ui.tlwBoxWord.setItem(i,1,QTableWidgetItem(row[5]))
            self.ui.tlwBoxWord.setItem(i,2,QTableWidgetItem(row[2]))
            i=i+1

    #Sửa từ vựng
    def edit_Vocabulary(self):
        indexRow=self.tlwBoxWord.currentRow()-1
        indexCol=self.tlwBoxWord.currentColumn()
        if indexRow <0:  # Nếu chưa chọn hàng để thay đổi 
            return
        value = self.tlwBoxWord.currentItem().text()
        word = Word()
        word.id=self.lstWord[indexRow][0]
        word.vocabulary=self.lstWord[indexRow][1]
        word.means=self.lstWord[indexRow][2]
        word.image=self.lstWord[indexRow][3]
        word.level_box=self.lstWord[indexRow][4]
        word.part_of_speech=self.lstWord[indexRow][5]
        #Ghi đè giá trị đã sửa 
        if indexCol == 0:
            if word.vocabulary==value: # Nếu ko có sự thay đổi
                return 
            word.vocabulary=value
        elif indexCol==1:
            if word.part_of_speech==value:
                return
            word.part_of_speech=value
        elif indexCol ==2:
            if word.means == value:
                return 
            word.means = value
        flag=update(word)

        if flag==1:
            showdialog("Update Success")
        else:
            showdialog("Update Fail")

    # Hàm xoá từ vựng
    def delete_Vocabulary(self):
        index=self.ui.tlwBoxWord.currentRow()-1
        if index < 0:
            return
        id = self.ui.lstWord[index][0]
        print(id)
        if delete(id)==1:
            showdialog("Delete Success")
            UIFunctions.mapping(self,self.ui.level)
        else:
            showdialog("Delete Fail")  
    
    #Lấy mỗi hộp 5 từ để luyên tập
    def findListPractice(self):
        self.ui.lstPractice=findPractice(-1,self.ui.level)
        UIFunctions.displayPractice(self)

    #Hiển thị từ vựng lên form Practice
    def displayPractice(self):
        # Làm mới Form
        self.ui.txtMeans.setText("")
        self.ui.lblPicture.setStyleSheet("border-image : url(image/000.jpg);") 
        self.ui.txtVocabulary.setText("")
        #self.ui.txtVoice.setText("")
        # Kiểm tra xem hôm nay đã luyện tập xong chưa
        # self.findListPractice()
        if len(self.ui.lstPractice)==0:
            showdialog("Hôm nay bạn đã hoàn thành bài tập rồi!")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            UIFunctions.mapping(self,self.ui.level)
            #frmPractice.close(self)
        else:
            #Hiển thị giá trị lên form
            word = self.ui.lstPractice[0]
            self.ui.txtMeans.setText(word[2])
            if word[3]:
                self.ui.lblPicture.setStyleSheet("border-image : url(image/"+word[3]+");") 
            else:
                self.ui.lblPicture.setStyleSheet("border-image : url(image/000.jpg);") 
    #Hàm kiểm tra xem câu trả lời có chính xác hay không
    def isCorrect(self,vocabulary):

        voca=self.ui.txtVocabulary.toPlainText()
        print(self.ui.voice)
        if voca =="" or self.ui.voice =="":
            showdialog("Vui lòng điền đầy đủ")
            return 
        # voice=self.txtVoice.text()
        word = self.ui.lstPractice.pop(0)
        if vocabulary.lower() == voca.lower() or vocabulary.lower()==self.ui.voice.lower():
            self.ui.lstCorrect.append(word)
            updateStatus(word[0],1)
            showdialog("Correct")
            UIFunctions.displayPractice(self)
        else:
            self.ui.lstWrong.append(word)
            updateStatus(word[0],0)
            showdialog("wrong")
            UIFunctions.displayPractice(self)

    #Hàm nghe để kiểm tra phát âm
    def listenning(self):
        robot_ear =speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            print("Robot: I'm Listening")
            audio = robot_ear.record(mic,duration=2)
            
        try:
            self.ui.voice = robot_ear.recognize_google(audio)
            #self.txtVoice.setText(self.voice)
        except:
            self.voice ="..."
            #self.txtVoice.setText("...")
    # Đọc từ vựng ở trong ô text
    def speaking(self):
        voca = self.ui.txtVocabulary.toPlainText()
        if(spell.correction(voca)==voca):
            robot_mouth = pyttsx3.init()
            robot_mouth.say(voca)
            robot_mouth.runAndWait()
        else:
            robot_mouth = pyttsx3.init()
            robot_mouth.say("You are wrong")
            robot_mouth.runAndWait()
        
    #Xem lại những từ đã trả lời đúng và đã trả lời sai
    def reviewVocabulary(self):
        if self.ui.level >0:
            lstCorrect = findPractice(1,self.ui.level)
            lstWrong = findPractice(0,self.ui.level)
    
            self.ui.tlwBoxWord.setColumnCount(3)
            self.ui.tlwBoxWord.setRowCount(1)
            self.ui.tlwBoxWord.setItem(0,0, QTableWidgetItem("Vocabulary")) 
            self.ui.tlwBoxWord.setItem(0,1, QTableWidgetItem("Part Of Speech"))
            self.ui.tlwBoxWord.setItem(0,2, QTableWidgetItem("Means"))

            i=1
            for row in lstCorrect:
                self.ui.tlwBoxWord.setRowCount(i+1)
                self.ui.tlwBoxWord.setItem(i,0,QTableWidgetItem(row[1]))          
                self.ui.tlwBoxWord.setItem(i,1,QTableWidgetItem(row[5]))
                self.ui.tlwBoxWord.setItem(i,2,QTableWidgetItem(row[2]))
                #Tô màu
                self.ui.tlwBoxWord.item(i,0).setBackground(QtGui.QColor(0,255,0))
                self.ui.tlwBoxWord.item(i,1).setBackground(QtGui.QColor(0,255,0))
                self.ui.tlwBoxWord.item(i,2).setBackground(QtGui.QColor(0,255,0))
                i=i+1
            for row in lstWrong:
                self.ui.tlwBoxWord.setRowCount(i+1)
                self.ui.tlwBoxWord.setItem(i,0,QTableWidgetItem(row[1]))      
                self.ui.tlwBoxWord.setItem(i,1,QTableWidgetItem(row[5]))
                self.ui.tlwBoxWord.setItem(i,2,QTableWidgetItem(row[2]))
                #Tô màu
                self.ui.tlwBoxWord.item(i,0).setBackground(QtGui.QColor(255,0,0))
                self.ui.tlwBoxWord.item(i,1).setBackground(QtGui.QColor(255,0,0))
                self.ui.tlwBoxWord.item(i,2).setBackground(QtGui.QColor(255,0,0))
                i=i+1
        elif self.ui.level <=0:
        # Đổi tên Review thành Move
        # Hàm di chuyển từ vựng vào hộp 1
            index=self.ui.tlwBoxWord.currentRow()-1
            if index < 0:   # Trường hợp chọn header
                return
            word = self.ui.lstWord[index]
            if move(word[0])==1:
                showdialog("Move Success")
                UIFunctions.mapping(self,self.ui.level)
            else:
                showdialog("Move Fail")  

        
    # #Ẩn thanh top
    # def changedTopBar(self):
    #     #Nếu đang ở form source thì ẩn hết 
    #     if self.ui.level==0:
    #         self.ui.btn_edit.hide()
    #         self.ui.btn_delete.hide()
    #         self.ui.btn_review.hide()
    #         self.ui.btn_practice.hide()
    #         self.ui.btn_cancel.hide()
    #     elif self.ui.level >0:
    #         #Tạo button Edit
    #         self.ui.btn_edit = QPushButton(self.ui.frame_toggle)
    #         self.ui.btn_edit.setObjectName(u"btn_edit")
    #         self.ui.btn_edit.setMinimumSize(QSize(0, 40))
    #         self.ui.btn_edit.setStyleSheet(u"QPushButton {\n"
    # "	color: rgb(255, 255, 255);\n"
    # "	background-color: rgb(35, 35, 35);\n"
    # "	border: 0px solid;\n"
    # "}\n"
    # "QPushButton:hover {\n"
    # "	background-color: rgb(85, 170, 255);\n"
    # "}")

    #         self.ui.horizontalLayout.addWidget(self.ui.btn_edit)
    #         self.ui.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))

    # def hideButton(self):
    #     self.ui.btnCustom.hide()
          