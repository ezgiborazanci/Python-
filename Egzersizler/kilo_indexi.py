print("Boy kilo indeksi hesaplama")

boy=float(input("Boyunuzu metre cinsinden giriniz:" ))
kilo=int(input("Kilonuzu giriniz:" ))

bki=kilo / (boy**2)

if(bki<18.5):
    print("Zayıf...")
elif(18.5<=bki and bki<25):
    print("Normal...")
elif(25<=bki and bki<30):
    print("Fazla kilo...")
else:
    print("Obez...")
