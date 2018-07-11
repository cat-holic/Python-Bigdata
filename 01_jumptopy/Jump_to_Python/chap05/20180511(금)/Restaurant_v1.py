class Restaurant:
    def __init__(self):
        self.restaurant_name, self.cuisine_type = map(str, input("레스토랑 이름과 요리 종류를 선택하세요." \
                                                                 "(공백으로 구분) : ").split())

        self.describe_restaurant()
        self.open_restaurant()

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 %s이고 %s 전문점입니다" % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 %s 레스토랑 오픈했습니다. 어서오세요" % self.restaurant_name)


if __name__ == "__main__":
    res1 = Restaurant()
# #이들 정보를 출력하는 describe_restaurant() 메서드와 레스토랑이 열렸다는 메시지를 출력하는 open_restaurant()를 만드세요.
#
# describe_restaurant() 출력
#
# "저희 레스토랑 명칭은 [restaurant_name] 이고 [cuisine_type] 전문점입니다."
#
# open_restaurant() 출력
#
# "저희 [restaurant_name] 레스토랑 오픈했습니다. 어서오세요."
#
#
#
#
# - 클래스에서 restaurant 인스턴스를 만드시오. 두 속성을 각각 출력(print함수)하고 메서드를 모두 호출하시오.
#
#
#
#
# 프로그램 실행예)
#
#
#
#
#
# 레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : 띵호화 중식
#
#
#
#
# 저희 레스토랑 명칭은 '띵호화'이고 중식 전문점입니다.
#
# 저희 띵호화 레스토랑이 오픈했습니다.
