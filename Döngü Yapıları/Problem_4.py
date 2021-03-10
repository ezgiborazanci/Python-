toplam=0

while True:
    sayı=input("Lütfen bir sayı giriniz: ")
    if(sayı =='q'):
        print("Programdan çıkılıyor...")
        break
    sayı=int(sayı)
    toplam+=sayı
print("Toplam:",toplam)