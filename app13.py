# Messagebox
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
        self.btn1=QPushButton("Info")
        self.btn2=QPushButton("Warning")
        self.btn3=QPushButton("Error")
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
        if sender==self.btn1:
            QMessageBox.information(self,"แจ้งเตือน","รายละเอียดโปรแกรม")
        elif sender==self.btn2:
            QMessageBox.warning(self,"แจ้งเตือน","ข้อควรระวังในการใช้งาน")
        elif sender==self.btn3:
            QMessageBox.critical(self,"แจ้งเตือน","เกิดข้อผิดพลาดในโปรแรกม")

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()