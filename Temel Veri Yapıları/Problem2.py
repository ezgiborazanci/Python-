"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

"""

kilo = float(input("Lütfen kilonuzu giriniz:"))
boy = float(input("Lütfen boyunuzu giriniz:"))

kitle_indeksi = kilo / boy**2

print("Kilo: {}\n" "Boy:{}\n" "Beden Kitle İdeksiniz:{}\n" .format(kilo, boy,float(kitle_indeksi)))

