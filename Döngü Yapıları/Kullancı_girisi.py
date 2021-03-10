print(""""
*********
Kullanıcı girişi programı
*********
      """)
kullanıcı_adı="Ezgi"
parola="12345"
giriş_hakkı=0

while(giriş_hakkı<3):
    a = input("Kullanıcı adını giriniz:")
    b = input("Parola giriniz:")
    if(kullanıcı_adı!=a and parola==b):
        print("Kullanıcı adı yanlış")
        giriş_hakkı+=1
        continue
    elif(kullanıcı_adı==a and parola!=b):
        print("Parola yanlış")
        giriş_hakkı += 1
        continue
    elif(kullanıcı_adı==a and parola==b):
        print("Hoşgeldiniz")
        break
    else:
        print("3 kere yanlış girdiniz")
        break