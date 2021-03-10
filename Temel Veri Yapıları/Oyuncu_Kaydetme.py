print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunu Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad,soyad,takım]

print("Bilgiler kaydediliyor...")

print("Oyuncunun Adı: {}\n"  "Oyuncunu Soyadı: {}\n" "Oyuncunun Takımı:{}" .format(bilgiler[0],bilgiler[1],bilgiler[2]))
print('Bilgiler kaydedildi....')
