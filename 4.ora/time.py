ido=int(input("Kérek egy adott számotú másodtpercet: "))
ev=0
nap=0
ora=0
perc=0
if(ido==0):
    print("now")
else:
    if(ido//60>0):
        perc=int(ido/60)
        ido=ido-(perc*60)
        if(perc//60>0):
            ora=int(perc/60)
            perc=perc-ora*60
            if(ora//24>0):
                nap=int(ora/24)
                ora=ora-nap*24
                if(nap//365>0):
                    ev=int(nap/365)
                    nap=nap-ev*365

    else:
        if(ido<0):
            print("Minusz számokkal nem lehet operálni.")
if(ev==1):
    print(ev, " Year ")
else:
    if(ev>1):
        print(ev, " Years ")

if(nap==1):
    print(ev, " Day ")
else:
    if(nap>1):
        print(nap, " Days ")

if(ora==1):
    print(ora, " Hour ")
else:
    if(ora>1):
        print(ora, " Hours ")

if(perc==1):
    print(perc, " minute ")
else:
    if(perc>1):
        print(perc, " minutes ")

if(ido==1):
    print(ido, " Secound ")
else:
    if(ido>1):
        print(ido, " Secounds ")