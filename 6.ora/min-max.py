import random
n=[]
for number in range(20):
    n.append(random.randint(1,100))
m=100
for i in range(20):
    if(n[i]<m):
        m=n[i]
print( "Min: ",m)
for i in range(20):
    if(n[i]>m):
        m=n[i]
print("Max: ",m)