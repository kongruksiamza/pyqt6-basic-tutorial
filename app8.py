# จัดการ Widget ด้วย Method
from PyQt6.QtCore import QCoreApplication,QSize
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout

#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        self.setFixedSize(QSize(400,300))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        self.setLayout(hbox)
        for message in ["Open","Save","Exit"]:
            self.display_button(message,hbox)

    def display_button(self,text,layout):
        btn=QPushButton(text)
        btn.setFixedSize(QSize(100,50))
        layout.addWidget(btn)

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()