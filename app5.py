# horizontal box layout
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout

#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout(self)
        self.setLayout(hbox)
        #button widget
        btn1=QPushButton("1")
        btn2=QPushButton("2")
        btn3=QPushButton("3")
        #จัดวาง widget ใน layout
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()