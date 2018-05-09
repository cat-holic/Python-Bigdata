def make_sandwich(order_list):
    print("샌드위치를 만들겠습니다.")
    for i in order_list:
        print("%s 추가합니다"%i)
    print("\n여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")


def input_ingredient(message):
    if message == 1:
        order_list = []
        while True:
            order = input("안녕하세요. 원하시는 재료를 입력하세요: ")
            if order == "종료":
                print()
                break
            else:
                order_list.append(order)
    make_sandwich(order_list)


wait_message = int(input("안녕하세요. 저희 가게에 방문해 주세서 감사합니다.\n1. 주문\n2. 종료\n입력 : "))
input_ingredient(wait_message)