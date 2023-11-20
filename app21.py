# Multiple Windows
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ออกแบบหน้าต่าง
class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("เกี่ยวกับเรา")
        self.setFixedSize(QSize(400,300))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        #widget
        lb=QLabel("ผู้พัฒนาโปรแกรมคือ ก้องรักสยาม")
        #add widget to layout
        vbox.addWidget(lb)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        self.setFixedSize(QSize(350,250))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        #widget
        self.about=None
        btn1=QPushButton("เกี่ยวกับเรา")
        btn1.clicked.connect(self.display)
        #add widget to layout
        vbox.addWidget(btn1)

    def display(self):
        if self.about is None:
            self.about=AboutWindow()
            self.about.show()

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()