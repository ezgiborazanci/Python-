#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
# #Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

birinci_değer = int(input("Lütfen bir sayı giriniz:"))
ikinici_değer = int(input("Lütfen bir sayı giriniz:"))
ücüncü_değer = int(input("Lütfen bir sayı giriniz:"))

çarpımları = birinci_değer*ikinici_değer*ücüncü_değer

print("Birinci değer: {}\n" "İkinici değer:{}\n" "Üçüncü değer:{}\n" "Çarpımları:{}\n" .format(birinci_değer,ikinici_değer,ücüncü_değer,float(çarpımları)) )