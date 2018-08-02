import threading
from WeatherData import WeaTherDate
import time

g_weather_data = {}
g_Dehumidifier = False
g_Humidifier = False
g_Balcony_Windows = False
g_AI_Mode = False
debug_mode = False


def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트 모드")
    print("4. 프로그램 종료")


def print_device_status(device_name, device_status):
    print("%s 상태: " % device_name, end="")
    if device_status:
        print("작동")
    else:
        print("정지")


def check_device_status():
    print("\n--------- IOT기기 현재 상태 ---------")
    print_device_status('제습기', g_Dehumidifier)
    print_device_status('가습기', g_Humidifier)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)


def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 제습기")
    print("2. 가습기")
    print("3. 발코니(베란다) 창")


def control_device():
    global g_Dehumidifier, g_Humidifier, g_Balcony_Windows

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요 : "))

    if menu_num == 1:
        g_Dehumidifier = not g_Dehumidifier
    elif menu_num == 2:
        g_Humidifier = not g_Humidifier
    elif menu_num == 3:
        g_Balcony_Windows = not g_Balcony_Windows

    check_device_status()


def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Updata")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode:
            print("작동 중")
        else:
            print("중지")

    elif menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode:
            AI_thread.start()
            print("작동")
        else:
            print("중지")
    elif menu_num == 3:
        get_realtime_weather_info()


def AI_balcony_window(rain):
    global g_Balcony_Windows

    if rain > 0 and g_Balcony_Windows:
        g_Balcony_Windows = not g_Balcony_Windows
        print("창문이 닫혔습니다")


# 제습기 AI 관리
def AI_dehumidifier(humidity, h_min=40, h_max=60):
    global g_Dehumidifier

    if debug_mode:
        h_min = 30
        h_max = 50

    if not (h_max <= humidity) and not g_Dehumidifier:
        g_Dehumidifier = not g_Dehumidifier
        print("제습기가 작동합니다")
    elif humidity <= h_max and g_Dehumidifier:
        g_Dehumidifier = not g_Dehumidifier
        print("제습기가 종료됩니다")


def AI_humidifier(humidity, h_min=40, h_max=60):
    global g_Humidifier
    if debug_mode:
        h_min = 70
        h_max = 90

    if not (humidity <= h_min) and not g_Humidifier:
        g_Humidifier = not g_Humidifier
        print("가습기가 작동합니다")
    elif h_min <= humidity and g_Humidifier:
        g_Humidifier = not g_Humidifier
        print("가습기가 종료됩니다")


def AI_Action():
    global g_weather_data
    if debug_mode:
        debug_realtime_weather_info()
    else:
        get_realtime_weather_info()
    print("현재 습도 : ", g_weather_data['humidity'])
    print("강수량 : ", g_weather_data['rain'])
    AI_balcony_window(g_weather_data['rain'])
    AI_dehumidifier(g_weather_data['humidity'])
    AI_humidifier(g_weather_data['humidity'])


def get_realtime_weather_info():
    global g_weather_data
    weather_dic = WeaTherDate().get_rain_humidity()
    g_weather_data = weather_dic


def debug_realtime_weather_info(rain, humidy):
    global g_weather_data
    g_weather_data = {'rain': rain, 'humidity': humidy}


def AI_scheduler():
    AI_Action()
    while True:
        day_time = time.strftime("%M")
        if day_time == 30:
            AI_Action()
        time.sleep(60)


print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                   - 오진석 -")

AI_thread = threading.Thread(target=AI_scheduler, daemon=True)

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        check_device_status()
    elif menu_num == 2:
        control_device()
    elif menu_num == 3:
        smart_mode()
    elif menu_num == 4:
        break

    time.sleep(1)
