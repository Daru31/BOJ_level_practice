m = int(input())
n = int(input())
l = []
for i in range(m, n+1):
    e=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                e+=1
                break
        if e==0:
            l.append(i)

if len(l)<1:
    print(-1)
else:
    print(sum(l))
    print(min(l))
