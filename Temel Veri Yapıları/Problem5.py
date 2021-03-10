#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = int(input("Lütfen bir sayı giriniz:"))
b = int(input("Lütfen bir sayı giriniz:"))
print("İlk sayı:" "{}\n" "İkinci Sayı:" "{}\n" .format(a,b))

a,b = b,a

print("Sayılar değiştiriliyor...")
print("İlk sayı:" "{}\n" "İkinci Sayı:" "{}\n" .format(a,b))