# Image
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        #สร้าง layout และตั้งค่า
        hbox=QHBoxLayout()
        self.setLayout(hbox)
        #widget
        img = QPixmap("programmer.png")
        label = QLabel()
        label.setPixmap(img)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #add widget to layout
        hbox.addWidget(label)


#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()