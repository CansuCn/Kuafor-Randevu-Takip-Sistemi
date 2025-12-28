from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        Dialog.setMinimumSize(QtCore.QSize(300, 300))
        Dialog.setMaximumSize(QtCore.QSize(300, 300))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.frame.setMinimumSize(QtCore.QSize(300, 300))
        self.frame.setMaximumSize(QtCore.QSize(300, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 90, 202, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.isletme_kuafor_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.isletme_kuafor_pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.isletme_kuafor_pushButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.isletme_kuafor_pushButton.setFont(font)
        self.isletme_kuafor_pushButton.setStyleSheet("QPushButton {\n"
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
        self.isletme_kuafor_pushButton.setObjectName("isletme_kuafor_pushButton")
        self.verticalLayout.addWidget(self.isletme_kuafor_pushButton)
        self.musteri_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.musteri_pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.musteri_pushButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.musteri_pushButton.setFont(font)
        self.musteri_pushButton.setStyleSheet("QPushButton {\n"
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
        self.musteri_pushButton.setObjectName("musteri_pushButton")
        self.verticalLayout.addWidget(self.musteri_pushButton)
        self.baslik_lbl = QtWidgets.QLabel(self.frame)
        self.baslik_lbl.setGeometry(QtCore.QRect(20, 50, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.baslik_lbl.setFont(font)
        self.baslik_lbl.setObjectName("baslik_lbl")
        self.geri_pushButton = QtWidgets.QPushButton(self.frame)
        self.geri_pushButton.setGeometry(QtCore.QRect(190, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.geri_pushButton.setFont(font)
        self.geri_pushButton.setStyleSheet("QPushButton {\n"
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
        self.geri_pushButton.setObjectName("geri_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.isletme_kuafor_pushButton.setText(_translate("Dialog", "İşletme / Kuaför"))
        self.musteri_pushButton.setText(_translate("Dialog", "Müşteri "))
        self.baslik_lbl.setText(_translate("Dialog", "Kayıt Türünü Seçiniz:"))
        self.geri_pushButton.setText(_translate("Dialog", "Geri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
