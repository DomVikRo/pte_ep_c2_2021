try:
    a1 = int(input("Kérem az első elemet: "))
    a2 = int(input("Kérem a második elemet: "))
    n=int(input("Hányadik elemnek számoljam ki az értékét: "))
except ValueError:
    print("Hiba a beolvasás során")
q=float(a2/a1)
m=a2*q
i=2
while i<=n:
    m=m*q
print("A felhasznó által megadott elem értéke: "+m)
