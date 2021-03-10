print("Notları giriniz:")
vize1=float(input("1.vize notu:"))
vize2=float(input("2.vize notu:"))
final=float(input("Final notu:"))
gno=(vize1*30/100)+(vize2*30/100)+(final*40/100)
if(gno>=90):
    print("AA")
elif(gno>=85):
    print("BA")
elif(gno>=80):
    print("BB")
elif(gno>=75):
    print("CB")
elif(gno>=70):
    print("CC")
elif(gno>=65):
    print("DC")
elif(gno>=60):
    print("DD")
elif(gno>=55):
    print("FD")
else:
    print("FF")