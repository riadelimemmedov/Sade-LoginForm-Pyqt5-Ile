import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Istifadeci Giris Paneli')
        self.setGeometry(500,200,350,300)
        self.panel()
        self.elaqe_qur()
        
    def elaqe_qur(self):
        baglanti = sqlite3.connect('login_form.db')
        self.baglanti_cursor = baglanti.cursor()
        
        self.baglanti_cursor.execute('CREATE TABLE IF NOT EXISTS istifadeciler(istifadeci_adi TEXT,sifre TEXT)')
        
        baglanti.commit()
        
    def panel(self):
        
        self.istifadeciadi = QtWidgets.QLineEdit()
        self.istifadeciadi.setPlaceholderText('Kullanici Adi')
        self.istifadecisifresi = QtWidgets.QLineEdit()
        self.istifadecisifresi.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris_butonu = QtWidgets.QPushButton('Giris')
        self.yazi_yeri = QtWidgets.QLabel('')
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.istifadeciadi)
        v_box.addWidget(self.istifadecisifresi)
        v_box.addWidget(self.yazi_yeri)
        v_box.addStretch()
        v_box.addWidget(self.giris_butonu)
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.setLayout(h_box)
        
        self.giris_butonu.clicked.connect(self.login)
        
        self.show()
    
    def login(self):
        adi = self.istifadeciadi.text()
        sifre = self.istifadecisifresi.text()
        
        query = self.baglanti_cursor.execute('SELECT * FROM istifadeciler WHERE istifadeciadi=? AND parola=?',(adi,sifre))#inputdan gelen deyerleri gonderirik yeni bele bir deyerde olan setirleri sec bize eger yoxdursa demeli qeydiyyatdan kecmeyib istifaci
        
        netice = query.fetchall()
        
        if len(netice) == 0:
            self.yazi_yeri.setText('Bele Bir Istifadeci Adi Tapilmadi'.format(adi))
            
        else:
            self.yazi_yeri.setText('Xosgeldiniz'.format(adi))
        
        self.istifadeciadi.clear()
        self.istifadecisifresi.clear()
        
app = QtWidgets.QApplication(sys.argv)
data = Pencere()
sys.exit(app.exec())
