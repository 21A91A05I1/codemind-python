n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in range(len(a)):
    if i%2:
        s=s+a[i]
    else:
        p=p+a[i]
if(s-p==0):
    print("YES")
else:
    print("NO")