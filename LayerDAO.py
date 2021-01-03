
from Model import Word
import mysql.connector
from _datetime import date
def getConnection():
    # tạo đối tượng connection
    myconn = mysql.connector.connect(host = "127.0.0.1", user = "root",
        password = "123456", database = "NNLTTT")
    return myconn
# def getConnection():
#     # tạo đối tượng connection
#     myconn = mysql.connector.connect(host = "127.0.0.1", user = "jstD",
#         password = "Dung_2000", database = "NNLTTT")
#     return myconn
                                                               
def findAll(sql):
    # tạo đối tượng cursor
    myconn=getConnection()
    cur = myconn.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    return myresult


def delete(id):
    myconn=getConnection()
    cur = myconn.cursor()
    sql1="Delete from review where id_Word = %s"     # Xoá những từ trong bảng review do có liên kết khoá ngoại
    sql2="Delete from word where id = %s"       # Xoá từ có id=id
    par =(id,)
    try:
        cur.execute(sql1,par)
        myconn.commit()
        cur.execute(sql2,par)
        myconn.commit()
        return 1
    except:
        return 0

    
def find_by_level_box(level):
    myconn=getConnection()
    cur = myconn.cursor()
    sql = "select * from word where level_box= %s"
    par =(level,)
    cur.execute(sql,par)
    myresult = cur.fetchall()
    return myresult

def add(word):
    myconn=getConnection()
    cur = myconn.cursor()
    sql="Insert into word(vocabulary,means,image,level_box,part_of_speech) values(%s,%s,%s,%s,%s)"
    par =(word.vocabulary,word.means,word.image,word.level_box,word.part_of_speech)
    try:
        cur.execute(sql,par)
        myconn.commit()
        return 1
    except:
        return 0

def move(id):
    myconn=getConnection()
    cur = myconn.cursor()
    sql="Update word set level_box=1 where id=%s"
    par =(id,)
    try:
        cur.execute(sql,par)
        myconn.commit()
        return 1
    except:
        return 0    

def update(word):
    myconn=getConnection()
    cur = myconn.cursor()
    sql="Update word set vocabulary=%s,means=%s,image=%s,level_box=%s,part_of_speech=%s where id=%s"
    par =(word.vocabulary,word.means,word.image,word.level_box,word.part_of_speech,word.id)
    try:
        cur.execute(sql,par)
        myconn.commit()
        return 1
    except:
        return 0    

# Tìm ngày học gần nhất
def findMaxDate():
    myconn=getConnection()
    cur = myconn.cursor()
    sql = "select max(date_practice) from review"
    cur.execute(sql)
    myresult = cur.fetchone()
    if myresult[0] != None:
        return myresult[0]
    else:
        return date(2000,1,1)

# Thềm vào bảng review
def addReview(id):
    myconn=getConnection()
    cur = myconn.cursor()
    sql="Insert into review(id_Word) values(%s)"
    par =(id,)
    try:
        cur.execute(sql,par)
        myconn.commit()
        return 1
    except:
        return 0

# Lấy lên những từ cần phải luyện tập vào ngày hôm nay hoặc những từ đã luyện tập cần xem kết quả
# -1: chưa luyện tập
#  0: trả lời sai
#  1: trả lơi đúng
def findPractice(status,level):
    myconn=getConnection()
    cur = myconn.cursor()
    sql = "select word.* from word,review where word.id=review.id_Word and status=%s and level_box = %s and date_practice=%s "
    par =(status,level,date.today())
    cur.execute(sql,par)
    myresult = cur.fetchall()
    return myresult
    
# Cập nhật status là 1 nếu trả lời đúng, 0 nếu trả lời sai
def updateStatus(id,status):
    myconn=getConnection()
    cur = myconn.cursor()
    sql="update review set status = %s where id_Word = %s and date_practice= %s"
    par =(status,id,date.today())
    try:
        cur.execute(sql,par)
        myconn.commit()
        return 1
    except:
        return 0   

# Nếu trả lời đúng thì sẽ tăng thêm 1 level
def updateBox(Date_Old):
    myconn=getConnection()
    cur = myconn.cursor()
    sql="update word set level_box=level_box+1 where id in (select id_word from review where date_practice=%s and status=1)"

    par =(Date_Old,)
    try:
        cur.execute(sql,par)
        myconn.commit()
        return 1
    except:
        return 0 

#Đếm số từ vựng ở trong mỗi box
def countNumOfBox(level):
    myconn=getConnection()
    cur = myconn.cursor()
    sql = "select count(*) from word where level_box=%s "
    par =(level,)
    cur.execute(sql,par)
    myresult = cur.fetchone()
    return myresult[0]

def totalResult(dateFrom,dateTo):
    myconn=getConnection()
    cur = myconn.cursor()
    print(dateFrom.toString("yyyy-MM-dd"))
    print(dateTo.toString("yyyy-MM-dd"))
    sql = "select * from review where date_practice >=%s and date_practice <=%s  "
    par =(dateFrom.toString("yyyy-MM-dd"),dateTo.toString("yyyy-MM-dd"))
    cur.execute(sql,par)
    myresult = cur.fetchall()
    lst = []        # Lưu những ngày luyện tập ở đây
    for x in myresult:
        if not x[2] in lst:
            lst.append(x[2])
    lstTrue = []
    lstFalse = []
    lst.sort()
    for x in lst:
        countTrue = 0
        countFalse = 0
        for y in myresult:
            if y[2] == x:
                if y[1] == 1:
                    countTrue +=1
                elif y[1] == 0:
                    countFalse +=1
        lstTrue.append((countTrue,x))
        lstFalse.append((countFalse,x))
    return lstTrue,lstFalse
