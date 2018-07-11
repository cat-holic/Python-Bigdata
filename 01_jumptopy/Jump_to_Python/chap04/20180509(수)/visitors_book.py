with open("C:/bigdata/Jump_to_Python\chap04/20180509(수)/방명록.txt", 'r', encoding='utf-8') as f:
    visitors_list = []

    while True:
        visitors_temp = f.readline()
        if not visitors_temp: break
        visitors_list.append(visitors_temp.replace('\n', ''))
    check_name = input("이름을 입력하세요 : ")
    check_flag = False
    for i in visitors_list:

        name, birth = map(str, i.split(' '))
        if check_name == name:
            print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요."%check_name)
            check_flag = True
            break

if not check_flag:
    with open("C:/bigdata/Jump_to_Python\chap04/20180509(수)/방명록.txt", 'a', encoding='utf-8') as f:
        birth = input("생년월일을 입력하세요 (예:801212) : ")
        f.write("\n" + check_name + " " + birth)
        print("%s님 환영합니다. 아래 내용을 입력하셨습니다."% check_name)
        print("%s %s"%(check_name,birth))