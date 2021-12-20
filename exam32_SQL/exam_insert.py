import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

form_window = uic.loadUiType('./user_insert.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_insert.clicked.connect(self.btn_insert_slot)

    def btn_insert_slot(self):
        userID, userName,birthYear,addr,mobile, height = None, None, None, None, None, None
        userID = self.le_userid.text()
        if len(userID) > 8:
            self.le_userid.setText('')
            userID = None
        userName = self.le_username.text()
        if len(userName) > 10:
            self.le_username.setText('')
            userName = None
        birthYear = self.le_birthyear.text()
        try:
            birthYear = int(birthYear)
        except:
            self.le_birthyear.setText('')
            birthYear = None
        addr = self.le_addr.text()
        if len(addr) > 2:
            self.le_addr.setText('')
            addr = None###setText 는 덮어쓰는것
        mobile = self.le_mobile.text()
        if len(mobile) > 8:
            self.le_mobile.setText('')
            mobile = None
        height = self.le_height.text()
        if height =='':
            height = 'null'
        try:
            if height != 'null':
                height = int(height)
            height = int(height)
        except:
            self.le_height.setText('')
            height = None
        if userID != None and userName != None and birthYear != None and \
                addr != None and mobile != None and height != None:
           print('debug01')
           sql = '''insert into userTBL value(
                  "{}","{}",{},"{}","{}", {});'''.format(
                    userID, userName, int(birthYear), addr, mobile,height)
           self.insert(sql)
           print(sql)

    def insert(self, sql):
        conn = pymysql.connect(user='root',
            passwd='789632',   #자신의 비번 입력
            host='127.0.0.1',
            port=3306,
            db='shopdb',
            charset='utf8')


        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                print('debug03')
            conn.commit()
        except:
            print('conn error')
        finally:
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())