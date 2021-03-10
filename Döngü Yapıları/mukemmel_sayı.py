a=int(input("Lütfen sayı giriniz: "))

toplam=0
for i in range(1,a):
    if(a%i==0):
        toplam+=i
    #i+=1

if(toplam == a):
    print("{} mükemmel sayıdır".format(a))
else:
    print("{} mükemmel sayı degildir".format(a))



