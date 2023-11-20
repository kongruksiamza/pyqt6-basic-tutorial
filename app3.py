# label & button
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QPushButton

#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        lb=QLabel("Hello Python",self)
        lb.move(150,0)
        btn = QPushButton("Click",self)
        btn.move(150,50)


#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()