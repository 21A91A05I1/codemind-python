s=input()
x=0
for i in s:
    if s.count(i)==1:
        print(i)
        x=1
        break
else:
    print(-1)