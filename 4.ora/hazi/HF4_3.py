n=int(input("Kérem a kívánt sort: "))
a=""
i=0

while i<n:
    i += 1
    e=(n+1-i)/i
    a+=str(e)+" "

print(a)