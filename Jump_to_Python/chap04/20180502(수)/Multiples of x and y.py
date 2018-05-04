while True:
    x = int(input("x의 값을 입력하세요(0을 입력시 프로그램 종료) : "))
    if x is 0: break;
    y = int(input("y의 값을 입력하세요 : "))
    z = int(input("z의 값을 입력하세요 : "))

    total =[]
    for i in range(1,z+1):
        if i%x==0 and i%y==0: total.append(i)
        elif i%x==0: total.append(i)
        elif i%y==0: total.append(i)

    print(total)