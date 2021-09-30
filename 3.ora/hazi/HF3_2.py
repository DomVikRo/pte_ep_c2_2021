ar=int(input("Kérem a termék árát: "))
if(ar>=10000):
    print("A termékre 20% kedvezmény jár, a termék értéke : ",(ar*0.8)," Ft")
else:
    print("A termékre 10% kedvezmény jár, a termék értéke : ", (ar * 0.9), " Ft")