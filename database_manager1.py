from pymongo import MongoClient

class DataBaseManager:  
    def __init__(self, connection_string = "mongodb://localhost:27017/", db_name = "KuaforRandevuDB"):
        self.baglanti_basarili = False   

        try:
           
            self.client = MongoClient(connection_string)
            self.client.admin.command('ping')   
            self.db = self.client[db_name]

      
            self.kuaforler_col = self.db["kuaforler"]
            self.musteriler_col = self.db["musteriler"]


            self.baglanti_basarili = True
            print(f"MongoDB bağlantısı başarılı: {db_name}")

        except Exception as e:
            print(f"MongoDB bağlantı hatası: {e}")
            self.client = None
            self.db = None



    def kuafor_ekle(self, kuafor_verileri):
        
        if not self.baglanti_basarili:
            
            return None

        try: 
            
            result = self.kuaforler_col.insert_one(kuafor_verileri)
            
            return result.inserted_id
        
        except Exception as e:
            print(f"Kuaför ekleme hatası: {e}")
            return None        



    def musteri_ekle(self, musteri_verileri):
        
        if not self.baglanti_basarili:
            return None
        
        try:
           
            result = self.musteriler_col.insert_one(musteri_verileri)
            return result.inserted_id
        
        except Exception as e:
            print(f"Müşteri ekleme hatası: {e}")
            return None
        
        

    def kullanici_dogrula(self, e_posta, sifre):

        if not self.baglanti_basarili:
            return None, None
        try:
            
            kuafor_kullanici = self.kuaforler_col.find_one({
                "e_posta" : e_posta,
                "sifre_hash" : sifre
            })

            if kuafor_kullanici:
                return "Kuaför", kuafor_kullanici
                
            
            musteri_kullanici = self.musteriler_col.find_one({
                "e_posta" : e_posta,
                "sifre_hash" : sifre
            })
            if musteri_kullanici:
                return "Müşteri", musteri_kullanici
                
            return None, None
        except Exception as e:
            print(f"kullanıcı doğrulama hatası: {e}")
            return None, None
        



    def ilceye_gore_kuaforleri_getir(self, ilce):    
        
        query_sorgu = {"rol" : "Kuaför", "ilce" : ilce}
        return list(self.kuaforler_col.find(query_sorgu, {"isletme_adi" : 1, "_id" : 1}))
    


    
    def kuafor_guncelle(self, kuafor_id, yeni_veri):
       
        if not self.baglanti_basarili:
            return None
        
        try:
            
            result = self.kuaforler_col.update_one(
                {"_id" : kuafor_id},
                {"$set" : yeni_veri}
            )
            return result
        except Exception as e:
            print(f"Kuaför güncelleme hatası: {e}")
            return None
        
        
    
    def musteri_guncelle(self, musteri_id, yeni_veri):

        if not self.baglanti_basarili:
            return None
        
        try:
            result = self.musteriler_col.update_one(
                {"_id" : musteri_id},
                {"$set" : yeni_veri}
            )
            return result
        except Exception as e:
            print(f"Müşteri güncelleme hatası: {e}")
            return None
    
        

    def kuafor_sil(self, kuafor_id):
        if not self.baglanti_basarili:
            return False
        
        try:
            sonuc = self.kuaforler_col.delete_one({"_id" : kuafor_id})
            return sonuc.deleted_count > 0         
        except Exception as e:
            print(f"Silme hatası: {e}")
            return False
        

    
    def musteri_sil(self, musteri_id):
        if not self.baglanti_basarili:
            return False
        
        try: 
            sonuc = self.musteriler_col.delete_one({"_id" : musteri_id})
            return sonuc.deleted_count > 0
        except Exception as e :
            print(f"Silme hatası: {e}")
            return False


    def randevu_ekle(self, randevu_verisi):
        
        kuafor_id = randevu_verisi.get("kuafor_id")
        tarih = randevu_verisi.get("tarih")
        saat = randevu_verisi.get("saat")

        if not self.randevu_muasit_mi(kuafor_id, tarih, saat): 
            print(f"HATA: {saat} saati zaten dolu!")
            return "DOLU" 

        
        try: 
            
            sonuc = self.db.randevular.insert_one(randevu_verisi)
            return sonuc.inserted_id
        except Exception as e :
            print(f"MongoDB Randevu Ekleme Hatası: {e}")
            return None
        
        
    def randevulari_getir(self, kuafor_id, tarih):
        
        try:
            sorgu = {"kuafor_id": str(kuafor_id), "tarih": tarih}
            
            return list(self.db.randevular.find(sorgu).sort("saat", 1))
        except Exception as e :
            print(f"MongoDB Randevu Getirme Hatası: {e}")
            return []
        

    def randevu_muasit_mi(self, kuafor_id, tarih, saat):
        try:
            sorgu = {
                "kuafor_id" : str(kuafor_id),
                "tarih" : tarih,
                "saat" : saat
            }
            mevcut_randevu = self.db.randevular.find_one(sorgu)
            return mevcut_randevu is None 
        except Exception as e:
            print(f"Müsaitlik kontrol hatası: {e}")
            return False