from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 529)
        Dialog.setMinimumSize(QtCore.QSize(523, 529))
        Dialog.setMaximumSize(QtCore.QSize(523, 529))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 523, 529))
        self.frame.setMinimumSize(QtCore.QSize(523, 529))
        self.frame.setMaximumSize(QtCore.QSize(523, 529))
        self.frame.setStyleSheet("color: rgb(245, 167, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 501, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.baslik_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.baslik_lbl.setFont(font)
        self.baslik_lbl.setStyleSheet("")
        self.baslik_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.baslik_lbl.setObjectName("baslik_lbl")
        self.verticalLayout.addWidget(self.baslik_lbl)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 380, 381, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uye_Ol_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.uye_Ol_pushButton.setFont(font)
        self.uye_Ol_pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(245, 167, 255);\n"
"border: none;\n"
"padding: 10px 20px;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #333333;\n"
"border: 1px solid black;\n"
"}")
        self.uye_Ol_pushButton.setObjectName("uye_Ol_pushButton")
        self.verticalLayout_3.addWidget(self.uye_Ol_pushButton)
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 150, 461, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.kuafor_adi_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.kuafor_adi_lbl.setFont(font)
        self.kuafor_adi_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.kuafor_adi_lbl.setObjectName("kuafor_adi_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kuafor_adi_lbl)
        self.kuaforAdi_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kuaforAdi_Yaz_le.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.kuaforAdi_Yaz_le.setFont(font)
        self.kuaforAdi_Yaz_le.setStyleSheet("QLineEdit:focus {    /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}")
        self.kuaforAdi_Yaz_le.setObjectName("kuaforAdi_Yaz_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kuaforAdi_Yaz_le)
        self.isim_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.isim_lbl.setFont(font)
        self.isim_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.isim_lbl.setObjectName("isim_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.isim_lbl)
        self.isim_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.isim_Yaz_le.setFont(font)
        self.isim_Yaz_le.setStyleSheet("QLineEdit:focus {    /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}")
        self.isim_Yaz_le.setObjectName("isim_Yaz_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.isim_Yaz_le)
        self.sehir_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.sehir_lbl.setFont(font)
        self.sehir_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.sehir_lbl.setObjectName("sehir_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sehir_lbl)
        self.sehir_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.sehir_Yaz_le.setFont(font)
        self.sehir_Yaz_le.setStyleSheet("QLineEdit:focus{ \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}\n"
"\n"
"")
        self.sehir_Yaz_le.setObjectName("sehir_Yaz_le")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sehir_Yaz_le)
        self.soyisim_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.soyisim_Yaz_le.setFont(font)
        self.soyisim_Yaz_le.setStyleSheet("QLineEdit:focus {   /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}\n"
"")
        self.soyisim_Yaz_le.setObjectName("soyisim_Yaz_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.soyisim_Yaz_le)
        self.soyisim_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.soyisim_lbl.setFont(font)
        self.soyisim_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.soyisim_lbl.setObjectName("soyisim_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.soyisim_lbl)
        self.ilce_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.ilce_lbl.setFont(font)
        self.ilce_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.ilce_lbl.setObjectName("ilce_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ilce_lbl)
        self.ilce_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.ilce_Yaz_le.setFont(font)
        self.ilce_Yaz_le.setStyleSheet("QLineEdit:focus {\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}")
        self.ilce_Yaz_le.setObjectName("ilce_Yaz_le")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ilce_Yaz_le)
        self.e_posta_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.e_posta_lbl.setFont(font)
        self.e_posta_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.e_posta_lbl.setObjectName("e_posta_lbl")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.e_posta_lbl)
        self.sifre_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.sifre_lbl.setFont(font)
        self.sifre_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.sifre_lbl.setObjectName("sifre_lbl")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.sifre_lbl)
        self.e_posta_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.e_posta_Yaz_le.setFont(font)
        self.e_posta_Yaz_le.setStyleSheet("QLineEdit:focus {\n"
"background-color: #333333;\n"
"border: 2px #DDDDDD;\n"
"}")
        self.e_posta_Yaz_le.setObjectName("e_posta_Yaz_le")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.e_posta_Yaz_le)
        self.sifre_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.sifre_Yaz_le.setFont(font)
        self.sifre_Yaz_le.setStyleSheet("QLineEdit:focus {\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}")
        self.sifre_Yaz_le.setObjectName("sifre_Yaz_le")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sifre_Yaz_le)
        self.telNo_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.telNo_lbl.setFont(font)
        self.telNo_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.telNo_lbl.setObjectName("telNo_lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.telNo_lbl)
        self.telNo_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.telNo_le.setFont(font)
        self.telNo_le.setStyleSheet("QLineEdit:focus {    \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.telNo_le.setObjectName("telNo_le")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.telNo_le)
        self.geri_gitk_pushButton = QtWidgets.QPushButton(self.frame)
        self.geri_gitk_pushButton.setGeometry(QtCore.QRect(420, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.geri_gitk_pushButton.setFont(font)
        self.geri_gitk_pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(245, 167, 255);\n"
"border: none;\n"
"padding: 10px 20px;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #333333;\n"
"border: 1px solid black;\n"
"}")
        self.geri_gitk_pushButton.setObjectName("geri_gitk_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.baslik_lbl.setText(_translate("Dialog", "KUAFÖR KAYDI"))
        self.uye_Ol_pushButton.setText(_translate("Dialog", "ÜYE OL"))
        self.kuafor_adi_lbl.setText(_translate("Dialog", "Kuaför Adı:"))
        self.isim_lbl.setText(_translate("Dialog", "İsim:"))
        self.sehir_lbl.setText(_translate("Dialog", "Şehir:"))
        self.soyisim_lbl.setText(_translate("Dialog", "Soyisim:"))
        self.ilce_lbl.setText(_translate("Dialog", "İlçe:"))
        self.e_posta_lbl.setText(_translate("Dialog", "E-posta:"))
        self.sifre_lbl.setText(_translate("Dialog", "Şifre:"))
        self.telNo_lbl.setText(_translate("Dialog", "Telefon:"))
        self.geri_gitk_pushButton.setText(_translate("Dialog", "Geri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
