li = [-1,-3,-4,-6,-7,1,3,4,5,6,7];

liminus=[];
liplus=[];

for i in li:
    if i<0: liminus.append(i);
    elif i>0: liplus.append(i);
li = liminus+liplus;
print(li);