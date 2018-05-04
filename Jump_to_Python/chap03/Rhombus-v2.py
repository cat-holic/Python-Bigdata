#coding: cp949
print("마름모 출력프로그램 v2")

while True:
    floor = int(input("최대 밑변의 크기를 입력하세요.(단, 홀수만 입력. 또한 0을 입력시 종료) : "))
    if floor == 0: break
    line = int((floor+1)/2)
    i=0
    while i!=line:
        blank = line - i - 1
        star = 0
        while blank != 0:
            print(" ", end="")
            blank-=1
        while star != (2*i+1):
            print("*",end="")
            star+=1
        print("")
        i+=1
    i=line-1
    while i != 0:
        blank = line-i
        star = 2*i-1
        while blank !=0:
            print(" ",end="")
            blank-=1
        while star != 0:
            print("*",end="")
            star-=1
        print("")
        i-=1

