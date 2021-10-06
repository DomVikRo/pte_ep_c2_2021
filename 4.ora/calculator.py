parancs=""
while parancs!="0":
    parancs=input("Kérlek válasz az alábbi opciók közül:\n\t1 összeadás \n\t0 kilépés")
    if parancs=="1":
        num=False
        a=0
        b=0
        while not num:
            try:
                a = float(input("Kérem az első számot"))
                b = float(input("Kérem a második számot"))
                num=True
            except ValueError:
                print("Hiba a beolvasás során")


        print("A két szám összege: ",(a+b))
