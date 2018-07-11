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

    def __del__(self):
        print("{0} 레스토랑 문닫습니다".format(self.restaurant_name))


restList = []

for i in range(3):
    restList.append(Restaurant())

print("밤 10시가 되었습니다.")

"""
[레스토랑 ver2]

ver1에서 클래스의 세 가지 인스턴스를 만들고 describe_restaurant() 함수를 각 객체에서 호출하시오.

클래스에 __del__(self) 소멸자를 정의하여 영업 종료 메세지를 출력한다.




프로그램 실행 예)


레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : 포석정 한식

저희 레스토랑 명칭은 포석정 이고 한식 전문점입니다.

저희 포석정 레스토랑이 오픈했습니다.




레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : 띵호화 중식

저희 레스토랑 명칭은 띵호화 이고 중식 전문점입니다.

저희 띵호화 레스토랑이 오픈했습니다.




레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : 애프터스쿨 분식

저희 레스토랑 명칭은 애프터스쿨 이고 분식 전문점입니다.

저희 애프터스쿨 레스토랑이 오픈했습니다.




 저녁 10시가 되었습니다.




포석정 레스토랑 문닫습니다.

띵호화 레스토랑 문닫습니다.

애프터스쿨 레스토랑 문닫습니다."""
