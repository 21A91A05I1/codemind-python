n=int(input())
a=list(map(int,input().split()))
k=max(a)
s=0
for i in a:
    for j in range(1,k**2):
        if j*j==i:
            s=s+i;
print(s)