#Python ‘da dosyaya yazma ve dosyadan okuma programı
def Listeleme(dosyaAdi):
#Parametre olarak gelen dosyada bulunan kayıtları listeleme.
# Okumak için dosyanın açılmas
  with open(dosyaAdi) as f: # f adında bir dosya nesnesi oluşturuldu
    for satir in f:  # Satır satır okuma işlemi için döngü kuruldu
      print(int(satir))  # int veri türüne dönüştürme ve ekrana yazdırma


def Kaydet(dosyaAdi):
  # Pa
  with open(dosyaAdi, "w") as f:  # f adında yazma modunda bir dosya nesnesi oluşturuldu
    sayi = 0
    while sayi != 999:  # Kullanici 999 giresiye kadar dönen döngü kuruluyor
      sayi = int(input("Lütfen sayi giriniz..(Çıkış içi 999):"))
      if sayi != 999:
        f.write(str(sayi) + "\n")  # String veri türüne dönüşüm ve dosyaya kayıt
      else:
        break  # Döngüden çıkış


  def main():
    # Ana Program başlangıcı. Menülü seçim işlemleri ve çıkış.
    kontrol = False
    while not kontrol:
      secim = input("K)aydet L)isteleme S)onlandır: ")
      if secim == "K" or secim == "k":
        Kaydet(input("Kayıt Edilecek Dosya Adı Girin:"))
      elif secim == "L" or secim == "l":
        Listeleme(input("Kayıtların Okunacağı Dosya Adını Girin <:"))
      elif secim == "S" or secim == "s":
        done = True
      main()