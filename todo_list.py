class Gorev:
    def __init__(self, ad):
        self.ad = ad
        self.tamamlandi = False

    def tamamla(self):
        self.tamamlandi = True


class GorevYoneticisi:
    def __init__(self):
        self.gorevler = []

    def gorev_ekle(self, ad):
        yeni_gorev = Gorev(ad)
        self.gorevler.append(yeni_gorev)

    def gorev_sil(self, indeks):
        if 0 <= indeks < len(self.gorevler):
            del self.gorevler[indeks]

    def gorev_tamamla(self, indeks):
        if 0 <= indeks < len(self.gorevler):
            self.gorevler[indeks].tamamla()

    def gorevleri_goruntule(self):
        print("\n--- Görev Listesi ---")
        
        print("Tamamlanmayan Görevler:")
        tamamlanmayan_var = False  # Kontrol için
        for i, gorev in enumerate(self.gorevler):
            if not gorev.tamamlandi:
                print(f"{i}: {gorev.ad}")
                tamamlanmayan_var = True
        if not tamamlanmayan_var:
            print("Tüm görevler tamamlandı!")

        print("\nTamamlanan Görevler:\n")
        tamamlanan_var = False  # Kontrol için
        for i, gorev in enumerate(self.gorevler):
            if gorev.tamamlandi:
                print(f"{i}: {gorev.ad}")
                tamamlanan_var = True
        if not tamamlanan_var:
            print("Tamamlanan görev yok!")

    def dosyaya_kaydet(self, dosya_adi):
        with open(dosya_adi, 'w') as dosya:
            for gorev in self.gorevler:
                dosya.write(f"{gorev.ad},{gorev.tamamlandi}\n")

    def dosyadan_yukle(self, dosya_adi):
        try:
            with open(dosya_adi, 'r') as dosya:
                self.gorevler = []
                for satir in dosya:
                    ad, tamamlandi = satir.strip().split(',')
                    yeni_gorev = Gorev(ad)
                    yeni_gorev.tamamlandi = tamamlandi == 'True'
                    self.gorevler.append(yeni_gorev)
        except FileNotFoundError:
            print("Dosya bulunamadı. Yeni bir liste oluşturuluyor.")


def ana_menu():
    yonetici = GorevYoneticisi()
    yonetici.dosyadan_yukle('gorevler.txt')

    while True:
        print("\n1. Görev Ekle")
        print("2. Görevi Tamamlandı Olarak İşaretle")
        print("3. Görev Sil")
        print("4. Görevleri Görüntüle")
        print("5. Çık ve Kaydet")
        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            ad = input("Görev adını girin: ")
            yonetici.gorev_ekle(ad)
        elif secim == '2':
            indeks = int(input("Tamamlanacak görevin numarasını girin: "))
            yonetici.gorev_tamamla(indeks)
        elif secim == '3':
            indeks = int(input("Silinecek görevin numarasını girin: "))
            yonetici.gorev_sil(indeks)
        elif secim == '4':
            yonetici.gorevleri_goruntule()
        elif secim == '5':
            yonetici.dosyaya_kaydet('gorevler.txt')
            print("Görevler kaydedildi. Çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    ana_menu()
