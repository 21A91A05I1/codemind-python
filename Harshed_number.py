n=int(input())
m=n
s=0
while n:
    d=n%10
    n//=10
    s=s+d
if m%s==0:
    print(True)
else:
    print(False)
