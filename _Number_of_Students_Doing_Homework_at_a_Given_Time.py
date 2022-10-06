n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(a)):
    for j in range(len(b)):
        if i==j and (a[i]<=k and b[j]>=k):
            c+=1
print(c)