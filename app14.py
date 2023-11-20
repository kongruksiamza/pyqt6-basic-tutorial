# Input Dialog
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        self.setFixedSize(QSize(400,250))
        #สร้าง layout และตั้งค่า
        vbox=QVBoxLayout()
        self.setLayout(vbox)
        #widget
        self.btn1=QPushButton("ป้อนชื่อ")
        self.btn2=QPushButton("ป้อนที่อยู่")
        self.btn3=QPushButton("เลือกเพศ")
        #signal 
        self.btn1.clicked.connect(self.showMessage)
        self.btn2.clicked.connect(self.showMessage)
        self.btn3.clicked.connect(self.showMessage)
        #add widget to layout
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

    def showMessage(self): #slot
        sender = self.sender()
        if sender == self.btn1:
           text,submit = QInputDialog.getText(self,"แจ้งเตือน","กรุณาป้อนชื่อของคุณ")
           if submit:
               QMessageBox.information(self,"แจ้งเตือน","สวัสดี "+text)
        elif sender==self.btn2:
            text , submit = QInputDialog.getMultiLineText(self,"แจ้งเตือน","กรุณาป้อนที่อยู่ของคุณ")
            if submit:
                QMessageBox.information(self,"แจ้งเตือน","ที่อยู่ของคุณ "+text)
        elif sender==self.btn3:
            items=["ชาย","หญิง","ไม่ระบุ"]
            text,submit = QInputDialog.getItem(self,"แจ้งเตือน","เลือกเพศ",items)
            if submit:
                QMessageBox.information(self,"แจ้งเตือน","เพศของคุณ "+text)

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()