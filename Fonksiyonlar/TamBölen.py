def tam_bölen(sayı):
    tambölenler=[]
    for i in range(2,sayı):
        if(sayı%i==0):
            tambölenler.append(i)
    return tambölenler

while True:
    sayı=input("sayı:")
    if(sayı=="q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayı=int(sayı)

        print("Tam bölenler:",tam_bölen(sayı))