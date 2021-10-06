i=1
j=1
al=""
while i<=10:
    while j<=10:
        k=i*j
        al+=str(k)+" "
        j+=1
    j=1
    i+=1
    print(al)
    al=""