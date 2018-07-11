# coding: UTF-8
with open("sample.txt", 'r', encoding="cp949") as f:
    lines = f.readlines()
    total = 0
    for i in lines:
        total += int(i)
    avg = total // len(lines)

with open("result.txt", 'w', encoding="UTF-8") as f:
    data = 'total = %d\naverage = %d' % (total, avg)
    f.write(data)
