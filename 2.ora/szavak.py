szav=["almaszár","misina","kerékgyartó","Égervölgyi tó","Flóra-pihenő","Tenkes","Malomvölgy","Zsolnay-kút"]
i=0
for x in szav:

    asz=szav[i]
    print(asz,"A szó hossza",len(asz));
    num=len(asz)
    i=i+1
i=0
print("10 karakter vagy annál hosszabb szavak listája: \n")
for x in szav:
    asz = szav[i]
    num = len(asz)

    if(num>=10):
        print(szav[i])
    i = i + 1