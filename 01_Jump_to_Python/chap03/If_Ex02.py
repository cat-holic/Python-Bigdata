# coding:cp949
money = int(input("얼마를 가지고 있습니까? "))
card = input("카드를 소유하고 있습니까?( y/n ) : ")
if card = 'y' :		card = True
else:			card = False

if money >= 3000:
    print("아키텍처 택시 분석 조건을 분석합니다")
else:
    if card ==True:
        #print("택시를 타고 가라") # 동일한 코드일 경우 중복
        print("[카드지원 택시]택시를 타고 가라") # 중복이 아닐경우 허용
        print("걸어가라")
