def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
i=1
while True:
    if prime(n+m+i):
        print(i)
        break
    i+=1