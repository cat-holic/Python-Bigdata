#coding: cp949
print("������ ������α׷� v1")
while True:
    floor = int(input("�ִ� �غ��� ũ�⸦ �Է��ϼ���.(��, Ȧ���� �Է�. ���� 0�� �Է½� ����) : "))
    if floor == 0 : break
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
     
