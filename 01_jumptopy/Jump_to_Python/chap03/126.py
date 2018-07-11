# cording : cp949

coffee_Current_Number = 10

while True:
    menu_choice = input("""<menu>
    1. 커피구매
    2. 커피잔량확인
    3. 프로그램 종료
    메뉴를 선택하세요: """)
    
    if menu_choice == "1":
        money = int(input("금액을 입력하세요: "))
        if money<300:
            print("금액이 %d원 모자랍니다." %(300-money))
        elif money == 300:
            print("커피를 줍니다")
            coffee_Current_Number -= 1
        elif money > 300:
            print("커피를 줍니다. \n여기 거스름돈 %d원입니다." %(money-300))
            coffee_Current_Number -= 1
        if not coffee_Current_Number:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다")
            break
    elif menu_choice == "2":
        print("현재 커피 잔량은 %d개 입니다." %coffee_Current_Number)
    elif menu_choice == "3":
        print("프로그램 종료를 선택하셨습니다. \n프로그램을 종료합니다")
        break
