#coding: cp949
# v3
# 나이를 입력 받아 나이에 따른 대구 IT공원 등급,입장료를 계산 하는 프로그램을 작성하시오.

# 0~3세(유아):무료
# 4~13세(어린이): 2000원
# 14~18세(청소년): 3000원
# 19~65세(성인): 5000원
# 66세 이상(노인): 무료

# [화면 출력]
# 나이를 입력하세요.
# 귀하는 []등급이며 요금은 []원 입니다.

# 요금을 입력하세요.
# (금액 미만 일 경우: "[]가 모자랍니다. 입력 하신 []를 반환합니다."
# 금액이 일치하는 경우: "감사합니다. 티켓을 발행합니다."
# 금액을 초과하는 경우: "감사합니다. 티켓을 발행하고 거스름돈 []를 반환 합니다."

# 나이를 입력 받아 나이에 따른 대구 IT공원 등급,입장료를 계산 하는 프로그램을 작성하시오.

while True:
    age=int(input("나이를 입력하세요. 입력 : "));
    rank="";

    if(age in range(0,4)): pay=0; rank="유아";
    elif(age in range(4,14)): pay=2000; rank="어린이";
    elif(age in range(14,19)): pay=3000; rank="청소년";
    elif(age in range(19,66)): pay=5000; rank="성인";
    elif(age >= 66): pay=0; rank="노인";
    elif(age < 0):
        print("다시 입력하세요");
        continue;

    if pay==0:
        print("고객님은 %s등급임으로 무료 입장 연령입니다"%rank);
        break;
    else:
        print("요금은 %s등급이며, %d원 입니다"%(rank,pay));
        break;

if pay!=0:
    inputPay = int(input("요금을 입력하세요 : "));
    if inputPay<pay:
        print("%d원이 모자랍니다. 입력하신 %d를 반환합니다"%(pay-inputPay,inputPay));
    elif inputPay==pay:
        print("감사합니다. 티켓을 발행합니다");
    elif inputPay>pay:
        print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다"%(inputPay-pay));
