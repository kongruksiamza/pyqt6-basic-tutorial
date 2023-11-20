# Combobox
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
        self.data=["Python","C#","PHP","Java"]
        self.combobox = QComboBox()
        self.combobox.addItems(self.data)
        #signal 
        self.combobox.currentIndexChanged.connect(self.saveData)
        #add widget to layout
        vbox.addWidget(self.combobox)
    
    def saveData(self):
        index = self.combobox.currentIndex()
        QMessageBox.information(self,"แจ้งเตือน",'รายการที่เลือก = '+self.data[index])


#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()