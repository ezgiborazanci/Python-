#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
#sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

yakıt = int(input("Aracınızın kilometrede kaç litre yakıt harcadığını girin:"))
yol = int(input("Aracınızın kaç kilometre gittiğini girin:"))

tutar = yol*yakıt

print("Aracınızın kilometrede harcadığı yakıt miktarı:{}\n" "Aracınızın gittiği kilometre:{}\n" "Ödemeniz gereken toplam tutar:{} TL'dir.\n".format(yakıt,yol,tutar))
