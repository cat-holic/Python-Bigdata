import threading
import time

g_Balcony_Windows = False
g_AI_Mode = False


def update_scheduler():
    global g_Balcony_Windows
    while True:
        if not g_AI_Mode:
            continue
        else:
            time.sleep(3)
            g_Balcony_Windows = not g_Balcony_Windows


t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

while True:
    print("메뉴를 선택하세요")
    print("1. 장비 상태 조회")
    print("2. 인공지능 모드 변경")
    print("3. 종료")

    menu_num = int(input("메뉴 입력 : "))
    if menu_num == 1:
        print("발코니(베란다) 창문 : ", end='')
        if g_Balcony_Windows:
            print("열림")
        else:
            print("닫힘")
    elif menu_num == 2:
        print("인공지능 모드: ", end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode:
            print("작동")
        else:
            print("정지")
    else:
        break
