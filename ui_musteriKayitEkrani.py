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
        font.setWeight(75)
        self.baslik_lbl.setFont(font)
        self.baslik_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.baslik_lbl.setObjectName("baslik_lbl")
        self.verticalLayout.addWidget(self.baslik_lbl)
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(29, 149, 461, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Misim_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Misim_lbl.setFont(font)
        self.Misim_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.Misim_lbl.setObjectName("Misim_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Misim_lbl)
        self.Msoyisim_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Msoyisim_lbl.setFont(font)
        self.Msoyisim_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.Msoyisim_lbl.setObjectName("Msoyisim_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Msoyisim_lbl)
        self.Msehir_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Msehir_lbl.setFont(font)
        self.Msehir_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.Msehir_lbl.setObjectName("Msehir_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Msehir_lbl)
        self.Milce_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Milce_lbl.setFont(font)
        self.Milce_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.Milce_lbl.setObjectName("Milce_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Milce_lbl)
        self.Me_posta_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Me_posta_lbl.setFont(font)
        self.Me_posta_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.Me_posta_lbl.setObjectName("Me_posta_lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Me_posta_lbl)
        self.Misim_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Misim_Yaz_le.setFont(font)
        self.Misim_Yaz_le.setStyleSheet("QLineEdit:focus {    \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.Misim_Yaz_le.setObjectName("Misim_Yaz_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Misim_Yaz_le)
        self.Msoyisim_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Msoyisim_Yaz_le.setFont(font)
        self.Msoyisim_Yaz_le.setStyleSheet("QLineEdit:focus {    \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.Msoyisim_Yaz_le.setObjectName("Msoyisim_Yaz_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Msoyisim_Yaz_le)
        self.Msehir_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Msehir_Yaz_le.setFont(font)
        self.Msehir_Yaz_le.setStyleSheet("QLineEdit:focus {    \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.Msehir_Yaz_le.setObjectName("Msehir_Yaz_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Msehir_Yaz_le)
        self.Milce_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Milce_Yaz_le.setFont(font)
        self.Milce_Yaz_le.setStyleSheet("QLineEdit:focus {    \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.Milce_Yaz_le.setObjectName("Milce_Yaz_le")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Milce_Yaz_le)
        self.Me_posta_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Me_posta_le.setFont(font)
        self.Me_posta_le.setStyleSheet("QLineEdit:focus {    /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.Me_posta_le.setObjectName("Me_posta_le")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Me_posta_le)
        self.Msifre_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Msifre_lbl.setFont(font)
        self.Msifre_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.Msifre_lbl.setObjectName("Msifre_lbl")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Msifre_lbl)
        self.Msifre_Yaz_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.Msifre_Yaz_le.setFont(font)
        self.Msifre_Yaz_le.setStyleSheet("QLineEdit:focus {    /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.Msifre_Yaz_le.setObjectName("Msifre_Yaz_le")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Msifre_Yaz_le)
        self.MtelNo_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.MtelNo_lbl.setFont(font)
        self.MtelNo_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.MtelNo_lbl.setObjectName("MtelNo_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.MtelNo_lbl)
        self.MtelNo_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.MtelNo_le.setFont(font)
        self.MtelNo_le.setStyleSheet("QLineEdit:focus {    \n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD\n"
"}")
        self.MtelNo_le.setObjectName("MtelNo_le")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.MtelNo_le)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 380, 381, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uye_Olm_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.uye_Olm_pushButton.setFont(font)
        self.uye_Olm_pushButton.setStyleSheet("QPushButton {\n"
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
        self.uye_Olm_pushButton.setObjectName("uye_Olm_pushButton")
        self.verticalLayout_2.addWidget(self.uye_Olm_pushButton)
        self.geri_gitm_pushButton = QtWidgets.QPushButton(self.frame)
        self.geri_gitm_pushButton.setGeometry(QtCore.QRect(420, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.geri_gitm_pushButton.setFont(font)
        self.geri_gitm_pushButton.setStyleSheet("QPushButton {\n"
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
        self.geri_gitm_pushButton.setObjectName("geri_gitm_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.baslik_lbl.setText(_translate("Dialog", "MÜŞTERİ KAYDI"))
        self.Misim_lbl.setText(_translate("Dialog", "İsim:"))
        self.Msoyisim_lbl.setText(_translate("Dialog", "Soyisim:"))
        self.Msehir_lbl.setText(_translate("Dialog", "Şehir:"))
        self.Milce_lbl.setText(_translate("Dialog", "İlçe:"))
        self.Me_posta_lbl.setText(_translate("Dialog", "E-posta:"))
        self.Msifre_lbl.setText(_translate("Dialog", "Şifre:"))
        self.MtelNo_lbl.setText(_translate("Dialog", "Telefon:"))
        self.uye_Olm_pushButton.setText(_translate("Dialog", "ÜYE OL"))
        self.geri_gitm_pushButton.setText(_translate("Dialog", "Geri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
