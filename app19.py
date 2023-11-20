# LineEdit & TextEdit
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
#ออกแบบหน้าต่าง
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน")
        self.setFixedSize(QSize(350,250))
        #สร้าง layout และตั้งค่า
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        #nested layout
        grid = QGridLayout()
        grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        grid.setSpacing(10)
        vbox.addLayout(grid)

        #Input Name
        grid.addWidget(QLabel('ชื่อ-นามสกุล'),0,0)
        self.editName=QLineEdit()
        self.editName.textChanged.connect(self.previewData)
        grid.addWidget(self.editName,0,1)
        #Input Address
        grid.addWidget(QLabel('ที่อยู่'),1,0)
        self.editAddress=QTextEdit()
        self.editAddress.textChanged.connect(self.previewData)
        grid.addWidget(self.editAddress,1,1)

        #แสดงผล
        vbox.addWidget(QLabel('Preview'))
        self.showName = QLabel()
        self.showAddress = QLabel()
        vbox.addWidget(self.showName)
        vbox.addWidget(self.showAddress)

    def previewData(self):
        sender = self.sender()
        if sender==self.editName:
            self.showName.setText(sender.text())
        elif sender==self.editAddress:
            self.showAddress.setText(sender.toPlainText())


#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()