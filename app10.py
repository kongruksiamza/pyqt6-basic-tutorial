# ตกแต่ง widget ด้วย QSS
from PyQt6.QtCore import QCoreApplication,QSize,Qt
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout

#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        self.setFixedSize(QSize(800,600))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        hbox.setSpacing(20)
        # vbox=QVBoxLayout()
        # vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(hbox)
        for message in ["Open","Save","Exit"]:
            self.display_button(message,hbox)

    def display_button(self,text,layout):
        btn=QPushButton(text)
        btn.setFixedSize(QSize(100,50))
        btn.setStyleSheet(
            '''
            color:white;
            background-color:blue;
            font-size:20px;
            font-weight:bold;
            text-align:center;
            '''
        )
        layout.addWidget(btn)

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()