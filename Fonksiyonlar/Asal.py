def asalsayı(x):
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        for i in range(2,x):
            if(x%i==0):
                return False
        return True

while True:
    x=input("Sayı:")
    if(x=="q"):
        break
    else:
        x=int(x)
        if(asalsayı(x)):
            print(x,"Asal sayıdır")
        else:
            print(x,"Asal değil")