print("""
*************
ATM ye Hoşgeldiniz
işlemler;
1-Bakiye sorgulama
2-Para Yatırma
3-Para Çekme

Programdan çıkmak için 'q' ya basınız
*************
      """)

bakiye=1000

while True:
    seçim = input("Lütfen işlem seçimi yapınız:")
    if(seçim == "q"):
        print("Yine bekleriz")
        break
    elif(seçim=="1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif(seçim=="2"):
        miktar=int(input("Miktar giriniz:"))
        bakiye+=miktar


    elif(seçim=="3"):
        miktar = int(input("Miktar giriniz:"))
        if(miktar>bakiye):
            print("Bakiyeniz yetersiz")
            continue
        else:
            bakiye -=miktar

    else:
        print("Geçersiz işlem")




