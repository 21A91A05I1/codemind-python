k=int(input())
c=0
r=0
while k!=0:
    n,m=map(int,input().split())
    for i in range(n,m+1,1):
        r=i%10
        if r==2 or r==3 or r==9:
            c+=1
    print(c)
    k-=1
    c=0