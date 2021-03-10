a=input("Lütfen üçgen veya dörtgen seçiniz: ")

if(a=="Dörtgen"):
    x=int(input("kenar1:"))
    y=int(input("kenar2:"))
    z=int(input("kenar3:"))
    t=int(input("kenar4:"))
    if(x==y==z==t):
        print("Kare")
    elif((x==z and y==t) or (x==y and z==t)):
        print("Dikdörtgen")
    else:
        print("Dörtgen")


elif(a=="Üçgen"):
    a = int(input("kenar1:"))
    b = int(input("kenar2:"))
    c = int(input("kenar3:"))
    if(abs(b-c)<a<abs(b+c) and abs(a-c)<b<abs(a+c) and abs(b-a)<c<abs(b+a) ):
        if(a==b==c):
            print("Eşkenar Üçgen")
        elif((a==b and b!=c) or (a==c and b!=c) or (c==b and a!=c)):
            print("İkizkenar")
        else:
            print("Çeşitkenar")
    else:
        print("Üçgen belirtmiyor")

else:
    print("Geçersiz şekil")