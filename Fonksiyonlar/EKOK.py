def ekok(a,b):
    i=2
    çarpım=1
    while True:
        if(a%i==0 and b%i==0):
            a//=i
            b//=i
            çarpım*=i
        elif(a%i!=0 and b%i==0):
            b//=i
            çarpım*=i
        elif(a%i==0 and b%i!=0):
            a//=i
            çarpım*=i
        else:
            i+=1
        if(a==1 and b==1):
            break
    return çarpım



