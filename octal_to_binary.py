n=int(input())
b=0
d=0
i=0
import math
while n!=0:
    r=n%10
    n=n//10
    d=d+r*(math.pow(8,i))
    i+=1
binary=0
rem=0
i=1
while d!=0:
    rem=d%2
    d=d//2
    binary=binary+rem*i
    i*=10
print(int(binary))