n=int(input())
temp=n
sum=0
while n>0:
    r=n%10
    sum+=r**2
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
if sum==1 or sum==7:
    print('True')
else:
    print('False')
    