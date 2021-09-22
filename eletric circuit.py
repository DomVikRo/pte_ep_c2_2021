ora=25
fesz=230
iz=5*30
kli=1500
mos=1500
vas=2000
szam=ora*fesz-iz-kli-mos-vas
if(szam>0):
    print("Nem, a vasaló nem vágja le a biztosítékot")
else:
    print("A vasaló le vágja a biztosítékot")