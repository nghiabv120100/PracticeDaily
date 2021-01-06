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
import PySide2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk,Image
import matplotlib.pyplot as plt

spell = SpellChecker()
root= tk.Tk()
root.withdraw()

# Biến trạng thái của edit
# 1: Edit
# 2: Save of Edit
# 3: Save of Add
actionEdit=0 

def showdialog(mess):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        msg.setText(mess)
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Notification")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

class UIFunctions(MainWindow):
    #Hiển thị thông báo
    def message_box(self):
        root.withdraw()
        resp = tk.messagebox.askquestion ('Warning','Do you want to quit?',icon = 'warning')
        if resp=="yes":
            self.close()
        else:
            pass

    ## Upload image
    saveName="000.jpg"
    def openfn(self):
        root.withdraw()
        filename = filedialog.askopenfile()
        return filename
    def loadImage(self):
        f = UIFunctions.openfn(UIFunctions)
        if f == None:
            return
        temp = f.name.split('/')
        UIFunctions.saveName = temp[-1]
        img = Image.open(f.name)
        img.save("image/"+UIFunctions.saveName)
        self.ui.btn_image.setStyleSheet("border-image : url(image/"+UIFunctions.saveName+");") 

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
        global actionEdit
        if actionEdit ==2 or actionEdit ==3:        # Lúc đang thêm hoặc chỉnh sửa thì ko được chuyển sang chế độ khác
            showdialog("Bạn đang ở chế độ chỉnh sửa")
            return

        actionEdit=0
        self.ui.level=level
        self.ui.lstWord=find_by_level_box(level) 
        if self.ui.level <0:
            self.ui.btn_review.setText(QCoreApplication.translate("MainWindow", u"Move", None))
            self.ui.btn_practice.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        else:
            self.ui.btn_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))  
            self.ui.btn_practice.setText(QCoreApplication.translate("MainWindow", u"Practice", None)) 
                   
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
    # Hiển thị chi tiết từ vựng qua frame frm_addVocabulary
    def displayDetailVocabulary(self):
        global actionEdit
        if actionEdit ==2 or actionEdit ==3 : # Đang edit hoặc đang Add
            return 

        index=self.ui.tlwBoxWord.currentRow()-1
        if index < 0:
            return
        
        actionEdit=1        # Có thể edit

        word = self.ui.lstWord[index]
        self.ui.txt_vocabulary.setText(word[1])
        self.ui.txt_partofspeech.setText(word[5])
        self.ui.txt_meaning.setText(word[2])
        self.ui.txt_eg.setText(word[6])
        self.ui.btn_image.setStyleSheet("border-image : url(image/"+word[3]+");") 


    #Sửa từ vựng
    def edit_Vocabulary(self):

        global actionEdit
        if actionEdit ==0:
            return
        elif actionEdit ==1:
            UIFunctions.enableTextEdit(self) 
            actionEdit =2
            self.ui.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        elif actionEdit == 2:
            indexRow=self.ui.tlwBoxWord.currentRow()-1
            if indexRow <0:  # Nếu chưa chọn hàng để thay đổi 
                return
            word = Word()
            word.id=self.ui.lstWord[indexRow][0]
            word.vocabulary=self.ui.txt_vocabulary.toPlainText()
            word.means=self.ui.txt_meaning.toPlainText()
            word.image=UIFunctions.saveName
            word.level_box=self.ui.level
            word.part_of_speech=self.ui.txt_partofspeech.toPlainText()
            word.eg=self.ui.txt_eg.toPlainText()
            flag=update(word)
            if flag==1:
                actionEdit=0
                showdialog("Update Success")
                UIFunctions.mapping(self,self.ui.level)
                UIFunctions.clearTextEdit(self)
                UIFunctions.lockTextEdit(self)
                self.ui.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
            else:
                showdialog("Update Fail")
            actionEdit=0
        elif actionEdit == 3: # Thêm từ vựng
            word = Word()
            word.vocabulary=self.ui.txt_vocabulary.toPlainText()
            word.means=self.ui.txt_meaning.toPlainText()
            word.image=UIFunctions.saveName
            word.level_box=self.ui.level
            word.part_of_speech=self.ui.txt_partofspeech.toPlainText()
            word.eg=self.ui.txt_eg.toPlainText()
            flag=add(word)
            if flag==1:
                actionEdit=0
                showdialog("Addition Success")
                UIFunctions.mapping(self,self.ui.level)
                UIFunctions.clearTextEdit(self)
                UIFunctions.lockTextEdit(self)
                self.ui.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
            else:
                showdialog("Addition Fail")
            actionEdit=0

    #Huỷ thêm hoặc sửa từ vựng
    def cancelEditOrAdd(self):
        global actionEdit
        if actionEdit == 2 or actionEdit ==3 :
            actionEdit=0
            UIFunctions.clearTextEdit(self)
            UIFunctions.lockTextEdit(self)
            self.ui.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        else:
            pass


    # Hàm xoá từ vựng
    def delete_Vocabulary(self):
        global actionEdit
        if actionEdit !=1: # Khi nhấn vào cell của table thì action edit =1
            return 
        index=self.ui.tlwBoxWord.currentRow()-1
        if index < 0:
            return
        id = self.ui.lstWord[index][0]
        print(id)
        if delete(id)==1:
            showdialog("Delete Success")
            UIFunctions.mapping(self,self.ui.level)
            UIFunctions.clearTextEdit(self)
        else:
            showdialog("Delete Fail")  
    
    #Lấy mỗi hộp 5 từ để luyên tập
    def findListPractice(self):
        if self.ui.level >5 or self.ui.level==0:
            return
        elif self.ui.level < 1: # Đổi practice thành Add
            global actionEdit
            actionEdit=3
            self.ui.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Save", None))
            UIFunctions.enableTextEdit(self)
            UIFunctions.clearTextEdit(self)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.frmPractice)
            self.ui.lstPractice=findPractice(-1,self.ui.level)
            UIFunctions.displayPractice(self)

    #Hiển thị từ vựng lên form Practice
    def displayPractice(self):
        print("display")
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
        #Xoá hết từ xong danh sách vừa phát âm
        self.ui.lstVoice.clear()
        
        voca=self.ui.txtVocabulary.toPlainText()
        print(self.ui.voice)
        if voca =="" or self.ui.voice =="":
            showdialog("Vui lòng điền đầy đủ")
            return 
        # voice=self.txtVoice.text()
        word = self.ui.lstPractice.pop(0)
        if vocabulary.lower() == voca.lower() or vocabulary.lower() in self.ui.lstVoice:
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
        if len(self.ui.lstVoice) >=3 or self.ui.lstPractice[0][1] in self.ui.lstVoice :   # Nếu phát âm đúng hoặc 3 lần thì ko cho phát âm nữa
            return 

        robot_ear =speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            robot_ear.adjust_for_ambient_noise(mic) # Giảm độ ồn của mic
            print("Robot: I'm Listening")
            audio = robot_ear.record(mic,duration=0.5) 
            
        try:
            self.ui.voice = robot_ear.recognize_google(audio)
            print(self.ui.voice)
        except:
            self.ui.voice ="..."
        self.ui.lstVoice.append(self.ui.voice)
        if self.ui.voice ==self.ui.lstPractice[0][1]:
            self.ui.lbl_icon.setStyleSheet("border-image : url(image/correct-icon.png);") 
        else:
            self.ui.lbl_icon.setStyleSheet("border-image : url(image/wrong-icon.png);") 
        print(self.ui.lstVoice)
    
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
        if self.ui.level >=0:
            lstCorrect = findPractice(1,self.ui.level)
            lstWrong = findPractice(0,self.ui.level)

            if (self.ui.level==0):
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
                lstCorrect =findAllPractice(1)
                print(lstCorrect)
                lstWrong =findAllPractice(0)
            print(lstCorrect)
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
                self.ui.tlwBoxWord.item(i,0).setBackground(QColor(0,255,0))
                self.ui.tlwBoxWord.item(i,1).setBackground(QColor(0,255,0))
                self.ui.tlwBoxWord.item(i,2).setBackground(QColor(0,255,0))
                i=i+1
            for row in lstWrong:
                self.ui.tlwBoxWord.setRowCount(i+1)
                self.ui.tlwBoxWord.setItem(i,0,QTableWidgetItem(row[1]))      
                self.ui.tlwBoxWord.setItem(i,1,QTableWidgetItem(row[5]))
                self.ui.tlwBoxWord.setItem(i,2,QTableWidgetItem(row[2]))
                #Tô màu
                self.ui.tlwBoxWord.item(i,0).setBackground(QColor(255,0,0))
                self.ui.tlwBoxWord.item(i,1).setBackground(QColor(255,0,0))
                self.ui.tlwBoxWord.item(i,2).setBackground(QColor(255,0,0))
                i=i+1
        elif self.ui.level <0:
        # Đổi tên Review thành Move
        # Hàm di chuyển từ vựng vào hộp 1
            global actionEdit
            if actionEdit !=1: # Khi nhấn vào cell của table thì action edit =1
                return 
            index=self.ui.tlwBoxWord.currentRow()-1
            if index < 0:   # Trường hợp chọn header
                return
            word = self.ui.lstWord[index]
            if move(word[0])==1:
                showdialog("Move Success")
                UIFunctions.mapping(self,self.ui.level)
                UIFunctions.renameBox(self,1)
            else:
                showdialog("Move Fail")  

        
    def renameBox(self,level):
        numOfBox= countNumOfBox(level)
        exec('self.ui.btn_page_'+str(level+1)+'.setText("Box"+str(level)+" ("+str(numOfBox)+")")')

    # gán level
    def assignLevel(self,level):
        self.ui.level=level
        global actionEdit
        actionEdit=0
        if level >=0:
            self.ui.btn_review.setText(QCoreApplication.translate("MainWindow", u"Review", None))  

    #Mở khoá text edit
    def enableTextEdit(self):
        self.ui.txt_vocabulary.setReadOnly(False)
        self.ui.txt_partofspeech.setReadOnly(False)
        self.ui.txt_meaning.setReadOnly(False)
        self.ui.txt_eg.setReadOnly(False)
        self.ui.txt_vocabulary.setFocus()
        # self.ui.btn_image.setEnabled(True)


    #khoá text edit
    def lockTextEdit(self):
        self.ui.txt_vocabulary.setReadOnly(True)
        self.ui.txt_partofspeech.setReadOnly(True)
        self.ui.txt_meaning.setReadOnly(True)
        self.ui.txt_eg.setReadOnly(True)
        # self.ui.btn_image.setEnabled(False)

    #clear text edit
    def clearTextEdit(self):
        self.ui.txt_vocabulary.setText("")
        self.ui.txt_partofspeech.setText("")
        self.ui.txt_meaning.setText("")
        self.ui.txt_eg.setText("")
       

def drawGraph(dateFrom,dateTo):
    d1,d2 = totalResult(dateFrom,dateTo)
    Day = [x[1] for x in d1]
    Day = [str(x.day)+'-'+str(x.month) for x in Day]
    print(Day)
    trues = [x[0] for x in d1]
    print(trues)
    falses = [x[0] for x in d2]
    print(falses)
    plt.plot(Day,trues,label = 'Correct')
    plt.plot(Day,falses,label = 'Wrong')

    plt.title('Review total result')
    plt.xlabel('Date')
    plt.ylabel('Number Answers')
    plt.legend()
    plt.show()

def numberOfDays(y, m):
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30

