print(chr(65))
print(ord("A"))
A=65
print(A)
print(int("A5", base=16))


a,b=2,4
if a==4 or b!=4:
    print("nyert")
if a == 4 or b == 4:
    print("majdnem nyert")

num=1
while num<=4:
    if num!=2:
        print("vesztett")
    elif num==3:
        print("türelmet kérek")
    else:
        print("nyert")
    num+=1