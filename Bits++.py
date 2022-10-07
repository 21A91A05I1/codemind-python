x=int(input())
c=0
for i in range(x):
    k=input()
    if k == 'X++' or k == "++X":
        c+=1
    else:
        c-=1
print(c)