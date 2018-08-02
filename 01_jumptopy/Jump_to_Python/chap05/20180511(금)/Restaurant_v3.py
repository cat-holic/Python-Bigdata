class Restaurant:
    number_served = 0

    def __init__(self):
        self.restaurant_name, self.cuisine_type = map(str, input("레스토랑 이름과 요리 종류를 선택하세요." \
                                                                 "(공백으로 구분) : ").split())
        self.describe_restaurant()
        chk_open = input("레스토랑을 오픈하시겠습니까? (y/n) : ").lower()
        if chk_open == "y":
            self.open_restaurant()
            while True:
                chk_stat = input("어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : ").lower()
                if chk_stat == '0': self.reset_number_served(0)
                elif chk_stat == '-1': break
                elif chk_stat == 'p': self.check_customer_number()
                elif int(chk_stat) < 0:
                    print("잘못입력하였습니다. 다시 입력해주세요")
                    continue
                else: self.increment_number_served(int(chk_stat))

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다" % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요\n" % self.restaurant_name)

    def __del__(self):
        print("{0} 레스토랑 문닫습니다 ^^".format(self.restaurant_name))

    def reset_number_served(self, number):
        self.number_served = number
        print("손님 카운팅을 {0}으로 초기화 하였습니다.".format(0))

    def increment_number_served(self, number):
        self.number_served += number
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다." % number)

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다." % self.number_served)



res1 = Restaurant()

print("밤 10시가 되었습니다.")

"""
레스토랑 ver3]

ver1에서 기본값이 0인 number_served 속성을 추가하시오. 이 클래스에서 restaurant 객체를 만드시오.

레스토랑에서 서빙한 고객 숫자를 출력하고, 이 값을 바꿔서 다시 출력하시오

- 서빙한 고객 숫자를 지정하는 def reset_number_served(self, number)메서드를 추가하시오.

  새숫자로 이 메서드를 호출하고 값을 다시 출력하시오.

- 서빙한 고객 숫자를 늘리는 increment_number_served(number) 메서드를 추가하시오.

  원하는 숫자, 예를 들어 영업일 하루 동안 서빙한 숫자로 이 메서드를 호출 하시오.

- 서빙한 고객 숫자를 확인하는 def check_customer_number(self): 를 추가하시오.




프로그램 출력 예)


레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : 띵호화 중식




저희 레스토랑 명칭은 띵호화이고 중식 전문점입니다.

레스토랑을 오픈하시겠습니까? (y/n)y




저희 띵호화 레스토랑이 오픈했습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : 3.Homenetwork

손님 3명 들어오셨습니다. 자리를 안내해 드리겠습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : 5

손님 5명 들어오셨습니다. 자리를 안내해 드리겠습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : p

지금까지 총 8명 손님께서 오셨습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : 0




손님 카운팅을 0으로 초기화 하였습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : 6

손님 6명 들어오셨습니다. 자리를 안내해 드리겠습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : 3.Homenetwork

손님 3명 들어오셨습니다. 자리를 안내해 드리겠습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : p

지금까지 총 9명 손님께서 오셨습니다.




어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : -1

띵호화 레스토랑 문닫습니다."""
