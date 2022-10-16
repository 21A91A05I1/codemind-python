a=input()
b=set(a)
c=0
maxi=0
p=[]
for i in b:
    maxi=0
    for j in range(0,len(a)):
        if i==a[j]:
            c+=1
            maxi=max(c,maxi)
        else:
            c=0
    p.append(maxi)
print(max(p))