def ebob(a,b):
    x=max(a,b)
    liste=list()
    for i in range(2,x):
        if(a%i==0 and b%i==0):
            liste.append(i)

    return max(liste)

a=int(input("Lütfen sayı giriniz:"))
b=int(input("Lütfen sayı giriniz:"))
print(ebob(a,b))
