"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2

"""

a = int(input("Lütfen dik olan bir kenarı giriniz:"))
b = int(input("Lütfen dik olan diğer kenarı giriniz:"))

hp = (a**2 + b**2)**0.5

print("Birinci dik kenar:{}\n" "İkinci dik kenar:{}\n" "Hipotenüs:{}\n".format(a,b,float(hp)))
