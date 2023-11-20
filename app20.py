# Table Widget
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
        #widget
        headers=["ชื่อ","ตำแหน่ง","เงินเดือน"]
        employees=[
            ('ก้อง','โปรแกรมเมอร์',25000),
            ('โจ้','กราฟิก',28000),
            ('นัท','ฝ่ายการตลาด',45000),
            ('น้ำ','ฝ่ายบัญชี',40000),
            ('ชาลี','ฝ่ายขาย',50000)
        ]
        table=QTableWidget(len(employees),len(headers))
        #set headers
        for i , h in enumerate(headers):
            table.setHorizontalHeaderItem(i,QTableWidgetItem(h))
        #set row data
        for r , rows in enumerate(employees):
            for c , data in enumerate(rows):
                if c==2:
                    item = f'{data:,}'
                else:
                    item = str(data)
                table.setItem(r,c,QTableWidgetItem(item))
        
        #table style
        table.horizontalHeader().setStyleSheet('::section{background:pink}')
        table.verticalHeader().setStyleSheet('::section{background:red}')
        #add widget to layout
        vbox.addWidget(table)

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])

window = MainWindow()
window.show()
app.exec()