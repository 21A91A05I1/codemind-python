n=int(input())
a=list(map(int,input().split()))
for i in a:
    b=[]
    for j in a:
        if i>j:
            b.append(j)
    print(len(b),end=' ')
    b=[]