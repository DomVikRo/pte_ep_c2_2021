a=input("Kérem egy szót: ")
e=1

if(len(a)%2==0):
    h=int(len(a)/2)
    i=0
    a1=a[0:h]
    a2=a[(h):len(a)]
    while(i<h):

        if(a1[i]!=a2[len(a2)-1]):
            e=0
        i+=1
    if(e==0):
        print("A szó palindrome")
    else:
        print("A szó nem palindrome")
else:
    h = int(len(a) / 2)
    i = 0
    a1 = a[0:h]
    a2 = a[(h)+1:len(a)]
    while (i < h):

        if (a1[i] != a2[len(a2) - 1]):
            e = 0
        i += 1
    if (e == 0):
        print("A szó palindrome")
    else:
        print("A szó nem palindrome")
