# coding: cp949

f = open("D:/������/Bigdata/Jump_to_python/chap04/" +
         "20180504(��)\hello.txt", 'w')
f.write("hello")

for i in range(10):
    f.write("%d��° �����Դϴ�\n" % i)
f.close()

f = open("D:/������/Bigdata/Jump_to_python/chap04/" +
         "20180504(��)\hello.txt", 'r')

line = f.read()

print(line)
