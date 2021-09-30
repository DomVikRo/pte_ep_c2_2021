num=10
if num<10:
    print("A szám kisebb mint 10")
else:
    print("A szám nagyobb vagy egyenlő mint 10")

if num>100:
    print("nagyobb mint 100")
else:
    print("nem nagyobb mint 100")

if(num%2==0):
    print("A szám páros")
else:
    print("páratlan")

num2=30
if num2%num==0|num%num2==0:
    print("A szám osztója a másik szánka ")
else:
    print("A szám nem osztója a másik szánka ")

s1="alma"
if s1[0]==s1[-1]:
    print("A karakterek egyeznek")
else:
    print("A karakterek nem egyeznek meg")





if(num>0):
    print("A szám pozitív")
else:
    if (num==0):
        print("A szám nulla")
    else:
        print("A szám negatív")

str="almafa"
str2="almaszár"
if str[0:4]==str2[0:4]:
    print("egyenlőek")