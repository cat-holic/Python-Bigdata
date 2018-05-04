# coding: cp949

f = open("D:/오진석/Bigdata/Jump_to_python/chap04/" +
         "20180504(금)\hello.txt", 'w')
f.write("hello")

for i in range(10):
    f.write("%d번째 라인입니다\n" % i)
f.close()

f = open("D:/오진석/Bigdata/Jump_to_python/chap04/" +
         "20180504(금)\hello.txt", 'r')

line = f.read()

print(line)
