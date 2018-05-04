#coding: cp949
with open("sample.txt",'r') as f:
    lines = f.readlines()
    total = 0;
    for i in lines:
        total+= int(i)
    avg = total//len(lines)

with open("result.txt",'w') as f:
    f.write("total = %d\navarage = %d"%(total,avg))
