#coding: cp949

freeTicket = 3;
discountTicket = 5;
guestCount = 0;
# 나이 입력체크의 시작
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
    # 나이 입력체크의 끝
    
    # 요금 유형체크 시작
if pay!=0:
    while True:
        payment = int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드) : "));
        if payment in range(1,3):break;
        else: print("잘못된 입력을 하였습니다. 다시 입력하세요."); continue;
    # 현금일 경우
    if payment == 1:
        inputPay = int(input("요금을 입력하세요 : "));
        if inputPay<pay:
            print("%d원이 모자랍니다. 입력하신 %d를 반환합니다"%(pay-inputPay,inputPay));
        elif inputPay==pay:
            print("감사합니다. 티켓을 발행합니다");
        elif inputPay>pay:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다"%(inputPay-pay));
    # 카드일 경우
    elif payment == 2:
        print("공원 전용 신용 카드의 경우, 결제 금액의 10% 할인,\n60~65세 장년은 추가 5% 할인됩니다.\n");

        if age in range(60,66): creditCardPay = int(pay*0.9*0.95);
        else: creditCardPay = int(pay*0.9);

        print("%d원 결제되었습니다. 티켓을 발행합니다."%creditCardPay);
    # 요금 유형체크 끝

    
