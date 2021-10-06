a1=int(input("Kérem az első számot: "))
a2=int(input("Kérem a második számot: "))
n=int(input("Hányadik elem érdekel? "))
q=a2/a1
m=a2*q
i=3
while i<n:
    m=m*q
    i+=1
print("A kívánt szám értéke: "+m)