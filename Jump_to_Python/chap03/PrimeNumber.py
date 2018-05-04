a=int(input())
d=int(input())
li = []
for b in range(a,d+1):
    flag = True
    if b == 1:
        continue
    if b == 2 : 
        li.append(b)
        continue
    for j in range(2,b):
        if b % j == 0:
            flag = False
            break
    if flag:
        li.append(b)
print(sum(li))
print(min(li))
