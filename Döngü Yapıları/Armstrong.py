sayı=input("Sayı giriniz:")
bas_sayısı=len(sayı)
sayı=int(sayı)
toplam=0
basamak=0
gecici_sayı=sayı

while(gecici_sayı>0):
    basamak=gecici_sayı%10
    toplam+=basamak**bas_sayısı
    gecici_sayı//=10
if(toplam==sayı):
    print("Armstrong sayı")
else:
    print("Armstrong sayı değil")

