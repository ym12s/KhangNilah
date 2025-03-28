import sys
import json
import os
import faulthandler
import subprocess
import sqlite3
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from functools import partial
faulthandler.enable()
subprocess.run(["pyside6-uic", "src/__ui/form.ui", "-o", "src/__ui/ui_mainwindow.py"], check=True)
COFFEE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(COFFEE_DIR, "..") 

sys.path.append(SRC_DIR)
sys.stdout.reconfigure(encoding="utf-8")

UI_FILE = os.path.join(SRC_DIR, "__ui", "ui_mainwindow.py")
if not os.path.exists(UI_FILE):
    subprocess.run(["pyside6-uic", os.path.join(SRC_DIR, "__ui", "form.ui"), "-o", UI_FILE], check=True)
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QButtonGroup, QLabel, QWidget,
                                QLineEdit,  QGraphicsDropShadowEffect,
                                QInputDialog, QMessageBox, QTableView, QHeaderView
                                )
from PySide6.QtGui import (QIcon, QPixmap, QAction, QPainter,
                            QPainterPath, QColor,QPalette)
from PySide6.QtCore import QSize, Qt, QTimer,QEasingCurve,QVariantAnimation,Signal
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from datetime import datetime 
from reportlab.pdfgen import canvas
from src.__ui.ui_mainwindow import Ui_MainWindow
from src.coffee.Ym12 import ym12s
from src.coffee.Ym12Circle import ym12c
from src.coffee.YAi import yai
from src.coffee.YSql import get_connection, DB_PATH
from PySide6.QtWidgets import QLineEdit

def ensure_ui_compiled():
    try:
        ui_file = os.path.join(SRC_DIR, "__ui", "form.ui")
        output_file = os.path.join(SRC_DIR, "__ui", "ui_mainwindow.py")
        
        if not os.path.exists(output_file) and os.path.exists(ui_file):
            subprocess.run(["pyside6-uic", ui_file, "-o", output_file], check=True)
            
    except Exception as e:
        print(f"Error compiling UI: {e}")
        return False
    return True

# Gọi hàm này trước khi import Ui_MainWindow
ensure_ui_compiled()

class MainWindow(QMainWindow):
    def __init__(self, idNhanVien=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.idNhanVien = idNhanVien
        self.chucvu = self.layChucVu()
        self.resize(1320,820)
        self.timer = QTimer()
        self.setWindowTitle("Coffee MTU")  
        self.giohang = []
        self.matkhau = "123"
        
        self.loadMenu()
        self.shadowWidget()
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(DB_PATH)
        self.database.open()
        
        self.setupButtons()
        
        self.ui.comboBoxDB.currentTextChanged.connect(self.loadTable) 
        self.ui.btnMua.clicked.connect(self.thanhtoan)
        self.ui.btnAddDB.clicked.connect(self.themrowtable)
        self.ui.pushButton1.clicked.connect(self.AIRespone)
        self.ui.btnXGH.clicked.connect(self.xoagiohang)
        self.ui.btnXoaDB.clicked.connect(self.xoaDongChon)
        self.ui.btnUpdateDB.clicked.connect(self.capNhatDatabase)
        self.ui.btnXem.clicked.connect(self.xemHoaDonDaChon)
        
        if self.idNhanVien:
            self.ui.lblWelcome.setText(f"WELCOME {self.idNhanVien} COFFEE MTU")
        
        self.loadDataBase()
        self.ui.lbThanhtien_3.setText("0")
        self.ui.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.centralwidget.layout().setSpacing(0)
        self.buttons = [self.ui.btnMenu, self.ui.btnOrder,
                        self.ui.btnAdmin, self.ui.btnAI
                        ]
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)

       
        self.buttons[0].setChecked(True)
        self.buttons[0].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))  
        self.buttons[1].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))  
        self.buttons[2].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))  
        self.buttons[3].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4)) 
        
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            if btn:
                btn.clicked.connect(self.btnClick)
            if spinBoxSL and spinBoxSL.value() == 0:
                spinBoxSL.setVisible(False)
            
        self.ui.btnXGH.clicked.connect(self.xoagiohang)    
    def tongtien(self):
        tongTien = 0
        for i in range(1, 16):
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            lblGia = getattr(self.ui, f'lbgia{i}', None)

            if spinBoxSL and lblGia:
                soluong = spinBoxSL.value()
                giaMon = self.giagoc.get(i, 0)
                tongTien += soluong * giaMon
        if self.giohang:
            self.ui.lbThanhtien_3.setText(f"{tongTien:,.0f} VND".replace(",", "."))
            return tongTien
    def hoadon(self):
        thanhTien = self.tongtien()
        
        if thanhTien == 0:
            return
        
        try:
            for item in self.giohang:
                for i in range(1, 16):
                    pwg = getattr(self.ui, f'pwg{i}', None)
                    spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
                    
                    if spinBoxSL and pwg and hasattr(pwg, 'ImgID'):
                        if item["idMon"] == pwg.ImgID:
                            item["soLuong"] = spinBoxSL.value()

            tongSoLuong = 0
            for item in self.giohang:
                tongSoLuong += item['soLuong']
            
            
            conn = get_connection()
            tro = conn.cursor()
                
            tro.execute("""
                INSERT INTO tb_DonHang (idNhanVien, trangThaiDH, tongTien)
                VALUES (?, ?, ?)
            """, (self.idNhanVien, "Chờ xử lý", thanhTien))
                
            tro.execute("SELECT last_insert_rowid()")
            self.idDonHang = tro.fetchone()[0]
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"hoadon_{timestamp}.html"
            
            html_content = f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }}
                    .header {{
                        text-align: center;
                        margin-bottom: 30px;
                    }}
                    .title {{
                        font-size: 24px;
                        font-weight: bold;
                        color: #4CAF50;
                    }}
                    .info {{
                        margin: 20px 0;
                        padding: 10px;
                        background-color: #f9f9f9;
                        border-radius: 5px;
                    }}
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin: 20px 0;
                    }}
                    th, td {{
                        padding: 12px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }}
                    th {{
                        background-color: #4CAF50;
                        color: white;
                    }}
                    tr:nth-child(even) {{
                        background-color: #f9f9f9;
                    }}
                    .total {{
                        font-size: 18px;
                        font-weight: bold;
                        text-align: right;
                        margin-top: 20px;
                    }}
                    .footer {{
                        margin-top: 30px;
                        text-align: center;
                        color: #666;
                        font-style: italic;
                    }}
                </style>
            </head>
            <body>
                <div class="header">
                    <div class="title">COFFEE MTU</div>
                    <div>HÓA ĐƠN BÁN HÀNG</div>
                </div>
                
                <div class="info">
                    <p>Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                    <p>Nhân viên: {self.idNhanVien}</p>
                </div>

                <table>
                    <tr>
                        <th>Tên món</th>
                        <th>Số lượng</th>
                        <th>Đơn giá</th>
                        <th>Thành tiền</th>
                    </tr>
            """
            
            for item in self.giohang:
                thanh_tien = item['soLuong'] * item['giaMon']
                html_content += f"""
                    <tr>
                        <td>{item['tenMon']}</td>
                        <td>{item['soLuong']}</td>
                        <td>{item['giaMon']:,} VND</td>
                        <td>{thanh_tien:,} VND</td>
                    </tr>
                """
            
            html_content += f"""
                </table>
                
                <div class="total">
                    Tổng tiền: {thanhTien:,} VND
                </div>
                
                <div class="footer">
                    <p>Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi!</p>
                    <p>Hẹn gặp lại quý khách!</p>
                </div>
            </body>
            </html>
            """
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            tro.execute("""
                INSERT INTO tb_ChiTietDonHang (idDonHang, tongSoLuong, thanhTien, fileHtml)
                VALUES (?, ?,  ?, ?)
            """, (self.idDonHang, tongSoLuong, thanhTien, filename))
            
            conn.commit()
            conn.close()
            
            self.messsuccess()
            self.ui.lbThanhtien_3.setText("0 VND")
            os.startfile(filename)
            self.xoagiohang()
            self.giohang.clear()
            
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tạo hóa đơn: {str(e)}")
    def messsuccess(self):
        if hasattr(self, 'msg'):
            try:
                self.msg.done(0)  
                self.msg.deleteLater()  
            except:
                pass
            
        self.msg = QMessageBox(self)
        self.msg.setIcon(QMessageBox.Information)
        
        chiTietDonHang = " ĐƠN ĐÃ ĐƯỢC TẠO !!!\n\n"
        
        self.msg.setText(chiTietDonHang)
        self.msg.setWindowTitle("Thành công")
        
        self.msg.setStyleSheet("""
            QMessageBox {
                background-color: transparent;
                padding: 20px;
            }
            QMessageBox QLabel {
                background-color: transparent;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                font-size: 12px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QMessageBox QIcon {
                width: 20px;
                height: 20px;
            }
        """)
        
        self.msg.exec()
    def autoScroll(self):
        self.diemSrcoll = self.ui.scrollMenu.verticalScrollBar().value()
        self.timer.start(2) 
    def smScroll(self):
        scrollbar = self.ui.scrollMenu.verticalScrollBar()
        scrollbarMax = scrollbar.maximum()

        if self.diemSrcoll <  scrollbarMax:
            self.diemSrcoll += 0.1
            scrollbar.setValue(self.diemSrcoll)
        else:
            self.timer.stop()    
    def AIRespone(self):
        self.tinnhanUser = self.ui.lineEdit.text().strip()
        if not self.tinnhanUser:
            return
        self.ui.textBrowser.append(f"Bạn: {self.tinnhanUser}")
        self.ui.lineEdit.clear()

        self.thread = yai(self.tinnhanUser)
        self.thread.tinHieuPhanHoi.connect(self.AIDisplay)
        self.thread.start()
    def AIDisplay(self, phanHoi):
        txtDisplay = self.ui.textBrowser.toPlainText().split("\n")
        
        if not txtDisplay or not txtDisplay[-1].startswith("AI:"):
            self.ui.textBrowser.append(f"AI: {phanHoi}")
        else:
            txtDisplay[-1] = f"AI: {phanHoi}"
            self.ui.textBrowser.setPlainText("\n".join(txtDisplay)) 
    def formload (self):
        self.loadDataBase()
        self.ui.lbThanhtien_3.setText("0")
        self.ui.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.centralwidget.layout().setSpacing(0)
        self.buttons = [self.ui.btnMenu, self.ui.btnOrder,
                        self.ui.btnAdmin, self.ui.btnAI
                        ]
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)

       
        self.buttons[0].setChecked(True)
        self.buttons[0].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))  
        self.buttons[1].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))  
        self.buttons[2].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))  
        self.buttons[3].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4)) 
        self.buttons[4].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2)) 
        
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            if btn:
                btn.clicked.connect(self.btnClick)
            if spinBoxSL and spinBoxSL.value() == 0:
                spinBoxSL.setVisible(False)
                
        self.ui.btnXGH.clicked.connect(self.xoagiohang)    
    
    def loadDataBase(self):
       query = self.database.exec("SELECT name FROM sqlite_master WHERE type='table'")
       tbls = []
       while query.next():
            tbls.append(query.value(0))
            
       self.ui.comboBoxDB.addItems(tbls)
       
       if tbls:
          self.loadTable(tbls[0])    
    def capNhatDatabase(self):
        if not self.models:
            self.showMessage("Cảnh báo", "Không có dữ liệu để cập nhật!", QMessageBox.Warning)
            return
            
        if self.chucvu != "Quản lý":
            self.showMessage("Cảnh báo", "Bạn không có quyền cập nhật dữ liệu!", QMessageBox.Warning)
            return
            
        try:
            if self.models.submitAll():
                self.showMessage("Thành công", "Đã cập nhật dữ liệu!")
                self.ui.tblDB.setEditTriggers(QTableView.NoEditTriggers)
            else:
                self.showMessage("Lỗi", f"Lỗi khi cập nhật: {self.models.lastError().text()}", QMessageBox.Critical)
        except Exception as e:
            self.showMessage("Lỗi", f"Lỗi: {str(e)}", QMessageBox.Critical)
    def xoaDongChon(self):
        if not self.models:
            self.showMessage("Cảnh báo", "Không có dữ liệu để xóa!", QMessageBox.Warning)
            return
            
        if self.chucvu != "Quản lý":
            self.showMessage("Cảnh báo", "Bạn không có quyền xóa dữ liệu!", QMessageBox.Warning)
            return
            
        current_index = self.ui.tblDB.currentIndex()
        if not current_index.isValid():
            self.showMessage("Cảnh báo", "Vui lòng chọn dòng cần xóa!", QMessageBox.Warning)
            return
        
        if self.showConfirm("Xác nhận", "Bạn có chắc muốn xóa dòng đã chọn?") == QMessageBox.Yes:
            try:
                row = current_index.row()
                
                success = self.models.removeRow(row)
                
                if success and self.models.submitAll():
                    self.models.select()  
                    self.showMessage("Thành công", "Đã xóa dữ liệu!")
                else:
                    self.showMessage("Lỗi", f"Lỗi khi xóa: {self.models.lastError().text()}", QMessageBox.Critical)
                    self.models.revertAll()  
                
            except Exception as e:
                self.showMessage("Lỗi", f"Lỗi: {str(e)}", QMessageBox.Critical)
                self.models.revertAll()
    def loadTable(self, tblDB):
        if tblDB:
            self.models = QSqlTableModel(self, self.database)
            self.models.setTable(tblDB)
            self.models.select()
            
            self.ui.tblDB.setModel(self.models)
            
            if self.chucvu == "Quản lý":
                self.ui.tblDB.setEditTriggers(QTableView.DoubleClicked | QTableView.EditKeyPressed)
            else:
                self.ui.tblDB.setEditTriggers(QTableView.NoEditTriggers)
            
            header = self.ui.tblDB.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeToContents)
            
            self.ui.tblDB.setSelectionMode(QTableView.SingleSelection)
            self.ui.tblDB.setSelectionBehavior(QTableView.SelectRows)
            
            self.ui.btnAddDB.setVisible(self.chucvu == "Quản lý")
            self.ui.btnUpdateDB.setVisible(self.chucvu == "Quản lý")
            self.ui.btnXoaDB.setVisible(self.chucvu == "Quản lý")
    def themrowtable(self):
        if not self.models:
            self.showMessage("Cảnh báo", "Vui lòng chọn bảng trước!", QMessageBox.Warning)
            return
            
        if self.chucvu != "Quản lý":
            self.showMessage("Cảnh báo", "Bạn không có quyền thêm dữ liệu!", QMessageBox.Warning)
            return

        # Thêm dòng mới
        row = self.models.rowCount()
        self.models.insertRow(row)
        
        # Kết nối signal để kiểm tra khi người dùng submit
        def validate_and_submit():
            # Lấy record của dòng mới thêm
            record = self.models.record(row)
            
            # Kiểm tra từng field
            empty_fields = []
            for i in range(record.count()):
                field = record.field(i)
                if field.value() is None or str(field.value()).strip() == "":
                    empty_fields.append(field.name())
            
            # Nếu có field trống
            if empty_fields:
                self.showMessage(
                    "Lỗi",
                    f"Các trường sau không được để trống:\n- " + "\n- ".join(empty_fields),
                    QMessageBox.Warning
                )
                # Revert lại thay đổi
                self.models.revertAll()
                return False
                
            # Nếu tất cả đều hợp lệ
            if self.models.submitAll():
                self.showMessage("Thành công", "Đã thêm dữ liệu mới!")
                return True
            else:
                self.showMessage(
                    "Lỗi", 
                    f"Lỗi khi thêm dữ liệu: {self.models.lastError().text()}", 
                    QMessageBox.Critical
                )
                self.models.revertAll()
                return False

        # Kết nối signal khi người dùng submit
        self.models.beforeSubmit.connect(validate_and_submit)
        
        # Scroll đến dòng mới thêm
        self.ui.tblDB.scrollToBottom()
    def btnClick(self):
        sender = self.sender()
        if not sender:
            return
        
        btnName = sender.objectName()
        if not btnName.startswith("btnAdd"):
            return
        
        try:
            idMon = int(btnName.replace("btnAdd", ""))
        except ValueError:
            return

        conn = get_connection()
        tro = conn.cursor()
        tro.execute("SELECT idMon, hinhAnh, tenMon, giaMon FROM tb_Mon WHERE idMon = ?", (idMon,))
        row = tro.fetchone()
        conn.close()

        if not row or not row[1]:
            return
        
        self.idMon, hinhAnh, tenMon, giaMon = row

        for i in range(1, 16):
            pwg = getattr(self.ui, f'pwg{i}', None)
            if not pwg:
                continue
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
                
            if not hasattr(pwg, "daCoAnh"):
                pwg.daCoAnh = False
            if not hasattr(pwg, "ImgID"):
                pwg.ImgID = None
                
            if pwg.ImgID == idMon:
                spinBoxSL.setValue(spinBoxSL.value()+1)
                return

        for i in range(1, 16):
            lblName = getattr(self.ui, f'lbname{i}', None)
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            lblGia = getattr(self.ui, f'lbgia{i}', None)
            pwg = getattr(self.ui, f'pwg{i}', None)
            spinBoxSL.setValue(spinBoxSL.value()+1)
            if not all([lblName, spinBoxSL, lblGia, pwg]):
                continue
                
            if not pwg.daCoAnh:
                label = ym12c(hinhAnh, pwg)
                label.setGeometry(0, 0, label.parent().width(), label.parent().height())
                label.parent().resizeEvent = self.capNhatSizeAnh
                
                lblName.setText("Món: " + tenMon)
                lblGia.setText("Đơn giá: " + str(giaMon))
                spinBoxSL.setVisible(True)
                
                self.giohang.append({
                    "idMon": idMon,
                    "tenMon": tenMon,
                    "giaMon": giaMon,
                    "soLuong": 1
                })
                
                if not hasattr(self, 'giagoc'):
                    self.giagoc = {}
                self.giagoc[i] = giaMon
                
                spinBoxSL.valueChanged.connect(lambda value, idx=i: self.capnhatgia(idx))
                spinBoxSL.valueChanged.connect(self.tongtien)
                
                pwg.daCoAnh = True
                pwg.ImgID = idMon
                sender.setText(f"Đã vào giỏ ")
                
                self.tongtien()
                break
    def thanhtoan(self):
        if self.giohang:
            idnhanvien = self.idNhanVien
            idDonHang = self.hoadon()
            if idDonHang:
                return idDonHang
        #       
    def capnhatgia(self,i):
        spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
        lblGia = getattr(self.ui, f'lbgia{i}', None)
        
        if not lblGia or not spinBoxSL:
            return
        if not hasattr(self, 'giagoc'):
            self.giagoc = {}
        giaMon = self.giagoc.get(i, 0)  
        soLuong = spinBoxSL.value()
        tongGia = soLuong * giaMon
        lblGia.setText("Đơn giá: "+str(tongGia))
    def xoagiohang (self):
        if self.giohang:
            for i in range(1, 16):
                lblName  =  getattr(self.ui, f'lbname{i}', None)
                spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
                pwg = getattr(self.ui, f'pwg{i}', None)
                lblGia = getattr(self.ui, f'lbgia{i}', None)
                if pwg:
                    pwg.daCoAnh = False
                    pwg.ImgID = None
                    lblGia.setText("")
                    for j in pwg.findChildren(QWidget):
                        j.deleteLater()
                        
                if spinBoxSL and spinBoxSL.setVisible(False):
                    spinBoxSL.setVisible(True)
                    spinBoxSL.setValue(0)
                    
                if lblGia:
                    lblGia.setText("")
                    
                if lblName:
                    lblName.setText("")
            self.ui.lbThanhtien_3.setText("0 VND") 
            self.giagoc.clear()
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            if btn:
                btn.setText("Add to Cart")
    def shadowWidget(self):
        
        self.a = []  
        wG = [ self.ui.wg1, self.ui.wg2, 
               self.ui.wg3, self.ui.wg4, self.ui.wg5
               , self.ui.wg6, self.ui.wg7, self.ui.wg8
               , self.ui.wg9, self.ui.wg10, self.ui.wg11,
               self.ui.wg12,self.ui.wg13,self.ui.wg14,self.ui.wg15,
               self.ui.pwg1,self.ui.pwg2,self.ui.pwg3,
               self.ui.pwg4,self.ui.pwg5,self.ui.pwg6,
               self.ui.pwg7,self.ui.pwg8,self.ui.pwg9,
               self.ui.pwg10,self.ui.pwg11,self.ui.pwg12,
               self.ui.pwg13,self.ui.pwg14,self.ui.pwg15,self.ui.wgThanhToan,self.ui.btnAddDB,
               self.ui.btnXoaDB,self.ui.btnUpdateDB,self.ui.WgPWG,
               self.ui.wdbtn,
               self.ui.wdtile,self.ui.wdtool
               
               ]
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(3)
        shadow1.setXOffset(5)
        shadow1.setYOffset(0)
        shadow1.setColor(QColor(0,0,0,180))
        self.ui.WgPWG.setGraphicsEffect(shadow1)
        for j in wG:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(0, 0, 0, 180))
            j.setGraphicsEffect(shadow)
            self.a.append(shadow)
    def loadMenu(self):
        conn = get_connection()
        tro  = conn.cursor()
        tro.execute("SELECT tenMon, hinhAnh From tb_Mon")
        dataMenu = tro.fetchall()
        conn.close()
        
        self.lbMenu = {}
        self.lblMenu = []
        
        for ind, (tenMon, hinhAnh) in enumerate(dataMenu, start=1):
            lbName = f"lblCost{ind}"
            wgName = f"wb{ind}"
            lbCost = getattr(self.ui, lbName,None)
            wb     = getattr(self.ui,wgName,None ) 
            
            if lbCost:
               self.lbMenu[ind] = lbCost
               self.lbMenu[ind].setText(tenMon) 
            
            if hasattr(self.ui,wgName):
                label = ym12s(hinhAnh,wb)
                label.setGeometry(0, 0, label.parent().width(), label.parent().height())
                label.parent().resizeEvent = self.capNhatSizeAnh         
                self.lblMenu.append(label)
                       
        label = ym12c(hinhAnh,self.ui.wg511)
        label.setGeometry(0, 0, label.parent().width(), label.parent().height())
        label.parent().resizeEvent = self.capNhatSizeAnh         
        self.lblMenu.append(label)       
    def capNhatSizeAnh(self, event):
        for i in self.lblMenu:
            i.setGeometry(0, 0, i.parent().width(), i.parent().height())    
    def resizeEvent(self, event):
        super().resizeEvent(event)
    def in_hoadon(self):
        if not self.giohang:
            QMessageBox.warning(self, "Cảnh báo", "Giỏ hàng trống!")
            return
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"hoadon_{timestamp}.html"
            
            html_content = f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }}
                    .header {{
                        text-align: center;
                        margin-bottom: 30px;
                    }}
                    .title {{
                        font-size: 24px;
                        font-weight: bold;
                        color: #4CAF50;
                    }}
                    .info {{
                        margin: 20px 0;
                        padding: 10px;
                        background-color: #f9f9f9;
                border-radius: 5px;
                    }}
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin: 20px 0;
                    }}
                    th, td {{
                        padding: 12px;
                text-align: left;
                        border-bottom: 1px solid #ddd;
                    }}
                    th {{
                        background-color: #4CAF50;
                color: white;
                    }}
                    tr:nth-child(even) {{
                        background-color: #f9f9f9;
                    }}
                    .total {{
                        font-size: 18px;
                        font-weight: bold;
                        text-align: right;
                        margin-top: 20px;
                    }}
                    .footer {{
                        margin-top: 30px;
                        text-align: center;
                        color: #666;
                        font-style: italic;
                    }}
                </style>
            </head>
            <body>
                <div class="header">
                    <div class="title">COFFEE MTU</div>
                    <div>HÓA ĐƠN TRƯỚC KHI IN</div>
                </div>
                
                <div class="info">
                    <p>Mã đơn hàng: {self.idDonHang}</p>
                    <p>Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                    <p>Nhân viên: {self.idNhanVien}</p>
                </div>

                <table>
                    <tr>
                        <th>Tên món</th>
                        <th>Số lượng</th>
                        <th>Đơn giá</th>
                        <th>Thành tiền</th>
                    </tr>
            """
            
            for item in self.giohang:
                thanh_tien = item['soLuong'] * item['giaMon']
                html_content += f"""
                    <tr>
                        <td>{item['tenMon']}</td>
                        <td>{item['soLuong']}</td>
                        <td>{item['giaMon']:,} VND</td>
                        <td>{thanh_tien:,} VND</td>
                    </tr>
                """
            
            tong_tien = sum(item['soLuong'] * item['giaMon'] for item in self.giohang)
            
            html_content += f"""
                </table>
                
                <div class="total">
                    Tổng tiền: {tong_tien:,} VND
                </div>
                
                <div class="footer">
                    <p>Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi!</p>
                    <p>Hẹn gặp lại quý khách!</p>
                </div>
            </body>
            </html>
            """
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            os.startfile(filename)
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể in hóa đơn: {str(e)}")
    def setupButtons(self):
        self.buttons = [
            (self.ui.btnMenu, 0),
            (self.ui.btnOrder, 2),
            (self.ui.btnAdmin, 5),
            (self.ui.btnAI, 3)
        ]
        
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)
        
        for btn, index in self.buttons:
            btn.setCheckable(True)
            self.buttonGroup.addButton(btn)
            btn.clicked.connect(lambda checked, idx=index: 
                self.ui.stackedWidget.setCurrentIndex(idx))
        
        self.buttons[0][0].setChecked(True)
        
        for i in range(1, 50):
            btn = getattr(self.ui, f"btnAdd{i}", None)
            if btn:
                btn.clicked.connect(self.btnClick)
    def layChucVu(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT chucVu FROM tb_NhanVien WHERE idNhanVien = ?"
            cursor.execute(query, (self.idNhanVien,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Lỗi khi lấy chức vụ: {e}")
            return None
        finally:
            conn.close()
    def themDongMoi(self):
        if not self.models:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn bảng trước!")
            return
        
        if self.chucvu != "Quản lý":
            QMessageBox.warning(self, "Cảnh báo", "Bạn không có quyền thêm dữ liệu!")
            return
        
        row = self.models.rowCount()
        self.models.insertRow(row)
        self.ui.tblDB.scrollToBottom()
    def showMessage(self, title, message, icon=QMessageBox.Information):
        msg = QMessageBox(self)
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        
        msg.setStyleSheet("""
           QMessageBox {
                background-color: transparent;
                padding: 20px;
            }
            QMessageBox QLabel {
                background-color: transparent;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
             QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                font-size: 12px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QMessageBox QIcon {
                width: 20px;
                height: 20px;
            }
        """)
        
        return msg.exec()
    def showConfirm(self, title, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        msg.setStyleSheet("""
            QMessageBox {
                background-color: transparent;
                padding: 20px;
            }
            QMessageBox QLabel {
                background-color: transparent;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                font-size: 12px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QMessageBox QIcon {
                width: 20px;
                height: 20px;
            }
        """)
        
        return msg.exec()
    def xemHoaDonDaChon(self):
        if self.models.tableName() != "tb_ChiTietDonHang":
            self.showMessage("Thông báo", "Vui lòng chọn bảng Chi tiết đơn hàng!", QMessageBox.Information)
            return
        
        current_index = self.ui.tblDB.currentIndex()
        if not current_index.isValid():
            self.showMessage("Cảnh báo", "Vui lòng chọn một đơn hàng để xem!", QMessageBox.Warning)
            return
        
        try:
            fileHtmlColumn = self.models.record().indexOf("fileHtml")
            
            fileHtmlIndex = self.models.index(current_index.row(), fileHtmlColumn)
            fileHtml = self.models.data(fileHtmlIndex)
            
            if fileHtml:
                if os.path.exists(fileHtml):
                    os.startfile(fileHtml)
                else:
                    self.showMessage("Cảnh báo", "Không tìm thấy file hóa đơn!", QMessageBox.Warning)
            else:
                self.showMessage("Cảnh báo", "Không có file hóa đơn cho đơn hàng này!", QMessageBox.Warning)
            
        except Exception as e:
            self.showMessage("Lỗi", f"Không thể mở hóa đơn: {str(e)}", QMessageBox.Critical)

        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            if btn:
                btn.clicked.connect(self.btnClick)
            if spinBoxSL and spinBoxSL.value() == 0:
                spinBoxSL.setVisible(False)
            
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            if btn:
                btn.clicked.connect(self.btnClick)
            if spinBoxSL and spinBoxSL.value() == 0:
                spinBoxSL.setVisible(False)
                
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            if btn:
                btn.setText("Add to Cart")