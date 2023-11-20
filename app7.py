# กำหนดขนาด Widget
from PyQt6.QtCore import QCoreApplication,QSize
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout

#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        self.setFixedSize(QSize(400,300))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout(self)
        #button widget
        btn1=QPushButton("1")
        btn2=QPushButton("2")
        btn2.setFixedSize(QSize(30,50))
        #จัดวาง widget ใน layout
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()