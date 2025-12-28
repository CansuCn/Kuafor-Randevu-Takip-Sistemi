import sys 
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

from ui_girisEkrani import Ui_Dialog as GirisFormu
from ui_butonlar import Ui_Dialog as ButonSecimFormu
from ui_musteriKayitEkrani import Ui_Dialog as MusteriKayitForm
from ui_kuaforKayitEkrani import Ui_Dialog as KuaforKayitForm

from ui_kuaforEkrani2 import Ui_MainWindow as KuaforAnaEkran
from ui_musteriEkrani3 import Ui_MainWindow as MusteriAnaEkran
from ui_kuaforProfili2 import Ui_MainWindow as KuaforProfil
from ui_musteriProfili import Ui_MainWindow as MusteriProfil

from database_manager import DataBaseManager



class BaseDialog(QtWidgets.QDialog):
    def __init__(self, onceki_ekran = None, db_manager = None):
        super().__init__()
        self.onceki_ekran = onceki_ekran
        self.db_manager = db_manager

    def geri_don(self):
        self.close()
        if self.onceki_ekran:
            self.onceki_ekran.show()



class GirisPenceresi(BaseDialog, GirisFormu):
    def __init__(self, db_manager = None):
        super().__init__(db_manager=db_manager)
        self.setupUi(self)

        self.kayitOl_pushButton.clicked.connect(self.kayit_secim_ekranini_ac)

        self.giris_pushButton.clicked.connect(self.kullanici_giris_yap)


    def kayit_secim_ekranini_ac(self):
        self.kayit_secim = KayitSecimPenceresi(self, self.db_manager) ##  ##
        self.kayit_secim.show()
        self.close()

    def kullanici_giris_yap(self):
        e_posta = self.e_posta_le.text().strip()
        sifre = self.sifre_le.text().strip()

        # === GEÇİCİ DEBUG KODU ===
        print(f"DEBUG: Girilen E-posta: {e_posta}")
        print(f"DEBUG: Girilen Şifre: {sifre}")
        # === DEBUG KODU BİTİŞİ ===


        if not e_posta or not sifre:
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen e_posta ve şifreyi girin.")
            return
        
        
        rol, kullanici_data = self.db_manager.kullanici_dogrula(e_posta, sifre)

        if rol:
            QtWidgets.QMessageBox.information(self, "Başarılı", f"Hoşgeldiniz, {rol}!")
            
            self.giris_basarili_yonlendir(rol, kullanici_data)

        else:
            QtWidgets.QMessageBox.critical(self, "Hata", "Kullanıcı adı veya şifre hatalı.")

    def giris_basarili_yonlendir(self, rol, kullanici_data):
                                               
        self.close()

        if rol == "Kuaför" : 
            self.kuafor_ekran = KuaforAnaPenceresi(kullanici_data, self.db_manager)
            self.kuafor_ekran.show()
            self.close()

        elif rol == "Müşteri":
            self.musteri_ekran = MusteriAnaPenceresi(kullanici_data, self.db_manager)
            self.musteri_ekran.show()
            self.close()
        
        else:
            QtWidgets.QMessageBox.critical(self, "Hata", "Tanımsız kullanıcı rölü.")
            



class KayitSecimPenceresi(BaseDialog, ButonSecimFormu):
    def __init__(self, onceki_ekran = None, db_manager = None):
        super().__init__(onceki_ekran, db_manager)
        self.setupUi(self)
                

        self.musteri_pushButton.clicked.connect(self.musteri_kayit_ac)        
        self.isletme_kuafor_pushButton.clicked.connect(self.kuafor_kayit_ac)
        
        
        if hasattr(self, "geri_pushButton"):
            self.geri_pushButton.clicked.connect(self.geri_don)

    
    def kuafor_kayit_ac(self):
        self.kuafor_kayit = KuaforKayitPenceresi(self, self.db_manager)
        self.kuafor_kayit.show()
        self.close()

    
    def musteri_kayit_ac(self):
        self.musteri_kayit = MusteriKayitPenceresi(self, self.db_manager)
        self.musteri_kayit.show()
        self.close()



class MusteriKayitPenceresi(BaseDialog, MusteriKayitForm):
    def __init__(self, onceki_ekran = None, db_manager = None):
        super().__init__(onceki_ekran, db_manager)
        self.setupUi(self)

        
        if hasattr(self, "geri_gitm_pushButton"):
            self.geri_gitm_pushButton.clicked.connect(self.geri_don)

        if hasattr(self, "uye_Olm_pushButton"):
            self.uye_Olm_pushButton.clicked.connect(self.musteri_kaydi_yap)

    def musteri_kaydi_yap(self):
        musteri_data = {
            "isim" : self.Misim_Yaz_le.text().strip(),
            "soyisim" : self.Msoyisim_Yaz_le.text().strip(),
            "sehir" : self.Msehir_Yaz_le.text().strip(),
            "ilce" : self.Milce_Yaz_le.text().strip(),
            "telefon" : self.MtelNo_le.text().strip(),
            "e_posta" : self.Me_posta_le.text().strip(),
            "sifre_hash" : self.Msifre_Yaz_le.text().strip(),
            "rol" : "Müşteri"
        }

        if any(not value for value in musteri_data.values()):
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")
            return
        
        inserted_id = None         

        if self.db_manager:     
            inserted_id = self.db_manager.musteri_ekle(musteri_data)

            if inserted_id:
                QtWidgets.QMessageBox.information(self, "Başarılı", "Müşteri kaydınız başarıyla oluşturuldu!")
                                  
                self.geri_don_ana_ekrana()

            else:
                QtWidgets.QMessageBox.critical(self, "Hata", "Kayıt sırasında bir sorun oluştu.")

    def geri_don_ana_ekrana(self):
        self.close()
        if self.onceki_ekran:
            self.onceki_ekran.geri_don()


    

class KuaforKayitPenceresi(BaseDialog, KuaforKayitForm):
    def __init__(self, onceki_ekran = None, db_manager = None):
        super().__init__(onceki_ekran, db_manager)
        self.setupUi(self)

        
        if hasattr(self, "geri_gitk_pushButton"):
            self.geri_gitk_pushButton.clicked.connect(self.geri_don)

        if hasattr(self, "uye_Ol_pushButton"):
            self.uye_Ol_pushButton.clicked.connect(self.kuafor_kaydi_yap)

    def kuafor_kaydi_yap(self):
        kuafor_data = {
            "isletme_adi": self.kuaforAdi_Yaz_le.text().strip(),
            "isim" : self.isim_Yaz_le.text().strip(),
            "soyisim" : self.soyisim_Yaz_le.text().strip(),
            "sehir" : self.sehir_Yaz_le.text().strip(),
            "ilce" : self.ilce_Yaz_le.text().strip(),
            "telefon": self.telNo_le.text().strip(),
            "e_posta" : self.e_posta_Yaz_le.text().strip(),
            "sifre_hash" : self.sifre_Yaz_le.text().strip(),
            "rol" : "Kuaför"

        }

        if any(not value for value in kuafor_data.values()):
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")
            return
        
        inserted_id  = None
        
        if self.db_manager:
            inserted_id = self.db_manager.kuafor_ekle(kuafor_data)


            if inserted_id:
                QtWidgets.QMessageBox.information(self, "Başarılı", "Kuaför kaydınız başarıyla oluşturuldu!")
                
                self.accept()
                self.geri_don_ana_ekrana()

            else:
                QtWidgets.QMessageBox.critical(self, "Hata", "Kayıt sırasında bir sorun oluştu.")

    def geri_don_ana_ekrana(self):
        self.close()

        if self.onceki_ekran : 
            self.onceki_ekran.geri_don()




class KuaforAnaPenceresi(QMainWindow, KuaforAnaEkran):
    def __init__(self, kullanici_data, db_manager):
        super().__init__()
        self.setupUi(self)
        self.kullanici_data = kullanici_data
        self.db_manager = db_manager

        
        self.setWindowTitle(f"Kuaför Paneli - {kullanici_data.get("isletme_adi")}")
        print(f"DEBUG: Kuaför Girişi Başarılı: {self.kullanici_data['isletme_adi']}")

        if hasattr(self, "bugun_pushButton"):
            self.bugun_pushButton.clicked.connect(self.bugune_git)
                                                                         
        if hasattr(self, "takvimK_calendarWidget"):       
            self.takvimK_calendarWidget.selectionChanged.connect(self.randevulari_yukle)

        if hasattr(self, "profilimK_pushButton"):
            self.profilimK_pushButton.clicked.connect(self.profil_ekranini_ac)


        self.takvimK_calendarWidget.selectionChanged.connect(self.randevulari_yukle) 
        
        self.setWindowTitle(f"Kuaför Paneli - {kullanici_data.get("isletme_adi", "Kuafor")}")
        self.randevulari_yukle()

    def bugune_git(self):
        
        self.takvimK_calendarWidget.setSelectedDate(QtCore.QDate.currentDate())



    def randevulari_yukle(self): 
        try:

            
            kuafor_id = str(self.kullanici_data["_id"])
            secili_tarih = self.takvimK_calendarWidget.selectedDate().toString("dd-MM-yyyy")


            
            randevular = self.db_manager.randevulari_getir(kuafor_id, secili_tarih)

            self.randevulari_listele(randevular, secili_tarih)

        except Exception as e:
            print(f"Randevu yükleme hatası: {e}")



    def randevulari_listele(self, randevular, secili_tarih):
        try:
           
            
            self.kuafor_listWidget.clear()
            
            
            if not randevular:
                self.kuafor_listWidget.addItem(f"📅 {secili_tarih} tarihinde randevu bulunamadı.")
                return

           
            for randevu in randevular:
                saat = randevu.get("saat", "--:--")
                musteri = randevu.get("musteri_adi", "Bilinmeyen")
                islem = randevu.get("islemler", "İşlem Yok")
                not_verisi = randevu.get("not", "")   
                
                not_metni = f"📝 (Not: {not_verisi})" if not_verisi else ""
                
                randevu_satiri = f"⏰ {saat}  |  👤 {musteri}  |  ✂️ {islem} {not_metni}"
                
                
                self.kuafor_listWidget.addItem(randevu_satiri)

            print(f"DEBUG: {secili_tarih} randevuları listeye başarıyla aktarıldı.")
        except Exception as e:
            print(f"Listeleme hatası: {e}")



    def profil_ekranini_ac(self):
        self.profil_penceresi = KuaforProfilPenceresi(self.kullanici_data, self.db_manager, self)
        self.profil_penceresi.show()
        self.close()   




class KuaforProfilPenceresi(QMainWindow, KuaforProfil):
    def __init__(self, kullanici_data, db_manager, ana_ekran_referansi):
        super().__init__()
        self.setupUi(self)
        self.kullanici_data = kullanici_data
        self.db_manager = db_manager
        self.ana_ekran_referansi = ana_ekran_referansi    

        self.bilgileri_yukle()

        
        self.bilgilerimiKaydet_pushButton.clicked.connect(self.kuafor_bilgilerini_kaydet)
        

        self.menuAna_Sayfaya_Don.aboutToShow.connect(self.ana_ekrana_don)
        self.menuOturumu_Kapat.aboutToShow.connect(self.oturumu_kapat)
        self.menuHesab_mi_Sil.aboutToShow.connect(self.hesabimi_sil)

    def bilgileri_yukle(self):
        self.profilK_isim_lineEdit.setText(self.kullanici_data.get("isim", ""))
        self.profilK_soyisim_lineEdit.setText(self.kullanici_data.get("soyisim", ""))
        self.isletmeAdi_lineEdit.setText(self.kullanici_data.get("isletme_adi", ""))
        self.isletmeTel_lineEdit.setText(self.kullanici_data.get("telefon", ""))
        self.isletmeEposta_lineEdit.setText(self.kullanici_data.get("e_posta", ""))
        self.isletme_ilce_lineEdit.setText(self.kullanici_data.get("ilce", ""))
        self.SifreDegistir_lineEdit.setText(self.kullanici_data.get("sifre_hash", ""))

    def kuafor_bilgilerini_kaydet(self):

        yeni_veri = {
            "isim": self.profilK_isim_lineEdit.text().strip(),
            "soyisim": self.profilK_soyisim_lineEdit.text().strip(),
            "isletme_adi": self.isletmeAdi_lineEdit.text().strip(),
            "telefon": self.isletmeTel_lineEdit.text().strip(),
            "e_posta": self.isletmeEposta_lineEdit.text().strip(),
            "ilce": self.isletme_ilce_lineEdit.text().strip(),
            "sifre_hash": self.SifreDegistir_lineEdit.text().strip()
        }
        
        try:
            
            self.db_manager.kuafor_guncelle(self.kullanici_data["_id"], yeni_veri)
            self.kullanici_data.update(yeni_veri)    
            QtWidgets.QMessageBox.information(self, "Başarılı", "Bilgileriniz güncellendi!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Güncelleme başarısız: {e}")

   

    def oturumu_kapat(self):
        QtWidgets.QApplication.instance().quit()

    def hesabimi_sil(self):
        onay = QtWidgets.QMessageBox.warning(
            self, "Hesap silme", "Hesabınızı silmek istediğinize emin misiniz? Bu işlemi geri alamazsınız!",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if onay == QtWidgets.QMessageBox.Yes:
            try:
                
                silindi_mi = self.db_manager.kuafor_sil(self.kullanici_data["_id"])

                if silindi_mi:
                    QtWidgets.QMessageBox.information(self, "Başarılı", "Hesabınızı silindi. Uygulama Kapatılıyor.")
                    QtWidgets.QApplication.instance().quit()

                else: 
                    QtWidgets.QMessageBox.critical(self, "Hata", "Hesap veritabanında bulunamadı.")
                
            except Exception as hata :
                QtWidgets.QMessageBox.critical(self, "Hata", f"İşlem başarısız: {hata}")



    def ana_ekrana_don(self):          
        self.close()
        if self.ana_ekran_referansi:
            self.ana_ekran_referansi.show()




class MusteriAnaPenceresi(QMainWindow, MusteriAnaEkran):
    def __init__(self, kullanici_data, db_manager):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Randevu Al - Hoşgeldiniz {kullanici_data.get("isim", "Müşteri")}")
        self.kullanici_data = kullanici_data
        self.db_manager = db_manager
 

        
        self.ilceleri_yukle()   


        print(f"DEBUG: Müşteri Girişi Başarılı: {self.kullanici_data['isim']}")


        self.randevu_kydt_pushButton.clicked.connect(self.ozeti_goster)
        self.sil_pushButton.clicked.connect(self.ozeti_temizle)
        self.onayla_pushButton.clicked.connect(self.randevu_onayla)


        if hasattr(self, "profilimM_pushButton"):
            self.profilimM_pushButton.clicked.connect(self.profil_ekranini_ac)


    def profil_ekranini_ac(self):
        self.profil_penceresi = MusteriProfilPenceresi(self.kullanici_data, self.db_manager, self)
        self.profil_penceresi.show()
        self.close()        



    def ilceleri_yukle(self):
        
        ilceler = ["Merkez", "Altıntaş" ,"Domaniç", "Emet", "Gediz", "Hisarcık", "Simav", "Tavşanlı"]
        
        if hasattr(self, "ilce_comboBox"):
            self.ilce_comboBox.clear()
            self.ilce_comboBox.addItem("...İlçe Seçiniz...")
            self.ilce_comboBox.addItems(ilceler)          

            
            self.ilce_comboBox.currentIndexChanged.connect(self.kuaforleri_filtrele)



    def kuaforleri_filtrele(self):
        
        secilen_ilce = self.ilce_comboBox.currentText()

        if secilen_ilce == "...İlçe Seçiniz...":
            self.kuafor_comboBox.clear()
            return
        
        try:
            
            kuaforler = self.db_manager.ilceye_gore_kuaforleri_getir(secilen_ilce)

            self.kuafor_comboBox.clear()
            self.kuafor_comboBox.addItem("...Kuaför Seçiniz...", None)

            for kuafor in  kuaforler:
                self.kuafor_comboBox.addItem(kuafor["isletme_adi"], str(kuafor["_id"]))

            print(f"DEBUG: {secilen_ilce} ilçesinde {len(kuaforler)} kuaför bulundu.")   

        except Exception as e:
            print(f"HATA: Filtreleme sırasında hata: {e}") 



    def ozeti_goster(self):
        try:
        
            kuafor = self.kuafor_comboBox.currentText()
            tarih = self.takvimM_calendarWidget.selectedDate().toString("dd.MM.yyyy")
            saat = self.timeEdit.time().toString("HH:mm")
            not_metni = self.islemDetay_Yaz_textEdit.toPlainText()

            
            sac = self.sac_comboBox.currentText()
            makyaj = self.makyaj_comboBox.currentText()
            bakim = self.bakim_comboBox.currentText()

            
            islem = f"{sac}, {makyaj}, {bakim}"


            self.tarih_label.setText(f"Tarih: {tarih} , Saat: {saat}")
            self.kuafor_adi_label.setText(f"Kuaför: {kuafor}")
            self.islem_label.setText(f"İşlem: {islem} \n Not: {not_metni}")

        except Exception as e:
            print(f"Hata oluştu: {e}")

    
    def ozeti_temizle(self):
        self.kuafor_adi_label.setText("Kuaför Adı: ")
        self.tarih_label.setText("Tarih: ")
        self.islem_label.setText("İşlem: ")
        self.islemDetay_Yaz_textEdit.clear()

        print("DEBUG: Özet ekranı temizlendi")

    
    def randevu_onayla(self):
        try:
            randevu_verisi = {
                "musteri_id" : self.kullanici_data["_id"],
                "musteri_adi" : f"{self.kullanici_data["isim"]} {self.kullanici_data["soyisim"]}",
                "kuafor_id" : self.kuafor_comboBox.currentData(), #kuafor id sini alıyoruz
                "kuafor_adi" : self.kuafor_comboBox.currentText(),
                "tarih" : self.takvimM_calendarWidget.selectedDate().toString("dd-MM-yyyy"),
                "saat" : self.timeEdit.time().toString("HH:mm"),
                "islemler" : f"{self.sac_comboBox.currentText()}, {self.makyaj_comboBox.currentText()}",
                "not" : self.islemDetay_Yaz_textEdit.toPlainText(),
                "durum" : "Onaylandı" 
            }

           
            if not randevu_verisi["kuafor_id"]:
                QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen bir kuaför seçiniz.")
                return
            
            
            sonuc = self.db_manager.randevu_ekle(randevu_verisi)

            if sonuc == "DOLU":  
                QtWidgets.QMessageBox.warning(self, "Saat Dolu",
                 f"Seçtiğiniz {randevu_verisi["saat"]} saatinde başka bir randevu bulunmaktadır. \n Lütfen başka bir saat seçiniz.")

            elif sonuc:
                
                QtWidgets.QMessageBox.information(self, "Başarılı", "Randevunuz oluşturuldu! Kuaför ekranında görünecektir.")
                self.ozeti_temizle

            else:
                
                QtWidgets.QMessageBox.critical(self, "Hata", "randevu kaydedilemedi.")

        except Exception as e :
            print(f"Onaylama Hatası: {e}")



class MusteriProfilPenceresi(QMainWindow, MusteriProfil):
    def __init__(self, kullanici_data, db_manager, ana_ekran_referansi):
        super().__init__()
        self.setupUi(self)
        self.kullanici_data = kullanici_data
        self.db_manager = db_manager
        self.ana_ekran_referansi = ana_ekran_referansi


        self.bilgileri_yukle()
        
        self.m_bilgilerimiKaydet_pushButton.clicked.connect(self.musteri_bilgilerini_kaydet)

        self.menuAna_Sayfaya_Don.aboutToShow.connect(self.ana_ekrana_don)
        
        if hasattr(self, "menuOturumu_Kapat"):
            self.menuOturumu_Kapat.aboutToShow.connect(self.oturumu_kapat)

        if hasattr(self, "menuHesab_m_Sil"):
            self.menuHesab_m_Sil.aboutToShow.connect(self.hesabimi_sil)

            
    def bilgileri_yukle(self):
       
        self.profilM_isim_lineEdit.setText(self.kullanici_data.get("isim", ""))
        self.profilM_soyisim_lineEdit.setText(self.kullanici_data.get("soyisim", ""))
        self.musteri_ilce_lineEdit.setText(self.kullanici_data.get("ilce", ""))
        self.musteri_Tel_lineEdit.setText(self.kullanici_data.get("telefon", ""))
        self.musteri_Eposta_lineEdit.setText(self.kullanici_data.get("e_posta", ""))
        self.musteri_SifreDegistir_lineEdit.setText(self.kullanici_data.get("sifre_hash", ""))


    def musteri_bilgilerini_kaydet(self):
        yeni = {
            "isim" : self.profilM_isim_lineEdit.text().strip(),
            "soyisim" : self.profilM_soyisim_lineEdit.text().strip(),
            "ilce" : self.musteri_ilce_lineEdit.text().strip(),
            "telefon" : self.musteri_Tel_lineEdit.text().strip(),
            "e_posta" : self.musteri_Eposta_lineEdit.text().strip(),
            "sifre_hash" : self.musteri_SifreDegistir_lineEdit.text().strip()
        }
        try:
            
            self.db_manager.musteri_guncelle(self.kullanici_data["_id"], yeni)
            self.kullanici_data.update(yeni)
            QtWidgets.QMessageBox.information(self, "Bilgi", "Bilgileriniz güncellendi!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Güncelleme başarısız: {e}")


    def oturumu_kapat(self):
        QtWidgets.QApplication.instance().quit()
        

    def hesabimi_sil(self):

        onay = QtWidgets.QMessageBox.warning(
            self, "Hesap Silme", "Hesabınızı silmek istediğinize emin misiniz? Bu işlem geri alamazsınız!",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if onay == QtWidgets.QMessageBox.Yes:
            try:
                
                silindi_mi = self.db_manager.musteri_sil(self.kullanici_data["_id"])

                if silindi_mi: 
                    QtWidgets.QMessageBox.information(self, "Başarılı", "Hesabınız silindi. Uygulama kapatılıyor.")
                    QtWidgets.QApplication.instance().quit()

                else:
                    QtWidgets.QMessageBox.critical(self, "Hata", "Hasap veritabanında bulunamadı.")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Hata", f"işlem sırasında bir hata oluştu: {e}")
        
    def ana_ekrana_don(self):
        self.close()
        if self.ana_ekran_referansi:
            self.ana_ekran_referansi.show()



if __name__ == '__main__':

    db_manager = DataBaseManager()  
    app = QtWidgets.QApplication(sys.argv)
    ana_ekran = GirisPenceresi(db_manager)
    ana_ekran.show()
    sys.exit(app.exec_())
