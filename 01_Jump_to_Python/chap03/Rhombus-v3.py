#coding: cp949
print("������ ������α׷� v3")
while True:
    floor = int(input("�ִ� �غ��� ũ�⸦ �Է��ϼ���.(��, Ȧ���� �Է�. ���� 0�� �Է½� ����) : "))
    if floor == 0:break
    maxFloorline = int((floor+1)/2)
    maxBorderline = floor+4
    i=0
    print(" ",end="")
    while i!=maxBorderline-3:
        print("-",end="")
        i+=1
    print()


    i=0
    while i!=maxFloorline:
        print("| ",end="")
        blank = maxFloorline - i - 1
        star = 0
        while blank != 0:
            print(" ", end="")
            blank-=1
        while star != (2*i+1):
            print("*",end="")
            star+=1
        while blank !=maxFloorline-i-1:
            print(" ",end="")
            blank+=1
        print(" |")
        i+=1


    i=maxFloorline-1
    while i != 0:
        print("| ",end="")
        blank = maxFloorline-i
        star = 2*i-1
        while blank !=0:
            print(" ",end="")
            blank-=1
        while star != 0:
            print("*",end="")
            star-=1
        while blank != maxFloorline - i:
            print(" ",end="")
            blank += 1
        print(" |")
        i-=1

    i=0
    print(" ",end="")
    while i!=maxBorderline-3:
        print("-",end="")
        i+=1
    print()

