#coding: cp949
li = [];
for i in range(1,1000):
    if i%3==0 and i%5==0:li.append(i);
    elif i%3==0:li.append(i);
    elif i%5==0:li.append(i);

print(sum(li));
