# Radio Button
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
        self.radio1=QRadioButton("ชาย")
        self.radio2=QRadioButton("หญิง")
        btnSave=QPushButton("บันทึก")
        #signal 
        btnSave.clicked.connect(self.saveData)
        #add widget to layout
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(btnSave)
    
    def saveData(self):
        if self.radio1.isChecked():
            QMessageBox.information(self,"แจ้งเตือน","รายการที่เลือก = "+self.radio1.text())
        elif self.radio2.isChecked():
            QMessageBox.information(self,"แจ้งเตือน","รายการที่เลือก = "+self.radio2.text())

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()