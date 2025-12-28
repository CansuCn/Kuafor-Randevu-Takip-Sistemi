from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 529)
        Dialog.setMinimumSize(QtCore.QSize(523, 529))
        Dialog.setMaximumSize(QtCore.QSize(523, 529))
        Dialog.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 523, 529))
        self.frame.setMinimumSize(QtCore.QSize(523, 529))
        self.frame.setMaximumSize(QtCore.QSize(523, 529))
        self.frame.setStyleSheet("color: rgb(245, 167, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(131, 370, 261, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.giris_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.giris_pushButton.setFont(font)
        self.giris_pushButton.setStyleSheet("QPushButton {    /*normal durumda*/\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(245, 167, 255);\n"
"border: none;\n"
"padding: 10px 20px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {  /*fare üzerine geldiğinde*/\n"
"background-color: #333333;\n"
"border: 1px solid black;\n"
"\n"
"}\n"
"")
        self.giris_pushButton.setObjectName("giris_pushButton")
        self.horizontalLayout_2.addWidget(self.giris_pushButton)
        self.kayitOl_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.kayitOl_pushButton.setFont(font)
        self.kayitOl_pushButton.setStyleSheet("QPushButton {    /*normal durumda*/\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(245, 167, 255);\n"
"border: none;\n"
"padding: 10px 20px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {  /*fare üzerine geldiğinde*/\n"
"background-color: #333333;\n"
"border: 1px solid black;\n"
"\n"
"}")
        self.kayitOl_pushButton.setObjectName("kayitOl_pushButton")
        self.horizontalLayout_2.addWidget(self.kayitOl_pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ana_baslik_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ana_baslik_lbl.setFont(font)
        self.ana_baslik_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ana_baslik_lbl.setObjectName("ana_baslik_lbl")
        self.verticalLayout.addWidget(self.ana_baslik_lbl)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 210, 301, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.e_posta_le = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.e_posta_le.setMinimumSize(QtCore.QSize(0, 20))
        self.e_posta_le.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.e_posta_le.setFont(font)
        self.e_posta_le.setStyleSheet("QLineEdit:focus {    /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}")
        self.e_posta_le.setAlignment(QtCore.Qt.AlignCenter)
        self.e_posta_le.setObjectName("e_posta_le")
        self.verticalLayout_2.addWidget(self.e_posta_le)
        self.sifre_le = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.sifre_le.setMinimumSize(QtCore.QSize(0, 20))
        self.sifre_le.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sifre_le.setFont(font)
        self.sifre_le.setStyleSheet("QLineEdit:focus {    /*fare üstüne geldiğinde*/\n"
"background-color: #333333;\n"
"border: 2px solid #DDDDDD;\n"
"}")
        self.sifre_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_le.setAlignment(QtCore.Qt.AlignCenter)
        self.sifre_le.setObjectName("sifre_le")
        self.verticalLayout_2.addWidget(self.sifre_le)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.giris_pushButton.setText(_translate("Dialog", "GİRİŞ"))
        self.kayitOl_pushButton.setText(_translate("Dialog", "KAYIT OL"))
        self.ana_baslik_lbl.setText(_translate("Dialog", "KUAFÖR RANDEVU TAKİP SİSTEMİ"))
        self.e_posta_le.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.e_posta_le.setPlaceholderText(_translate("Dialog", "E-POSTA"))
        self.sifre_le.setPlaceholderText(_translate("Dialog", "ŞİFRE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
