#coding: cp949

freeTicket = 3;
discountTicket = 5;
guestCount = 0;
while True:

    # ���� �Է�üũ�� ����
    while True:
        age=int(input("���̸� �Է��ϼ���. �Է� : "));
        rank="";

        if(age in range(0,4)): pay=0; rank="����";
        elif(age in range(4,14)): pay=2000; rank="���";
        elif(age in range(14,19)): pay=3000; rank="û�ҳ�";
        elif(age in range(19,66)): pay=5000; rank="����";
        elif(age >= 66): pay=0; rank="����";
        elif(age < 0):
            print("�ٽ� �Է��ϼ���");
            continue;

        if pay==0:
            print("������ %s��������� ���� ���� �����Դϴ�"%rank);
            break;
        else:
            print("����� %s����̸�, %d�� �Դϴ�"%(rank,pay));
            break;
        # ���� �Է�üũ�� ��
    
    # ��� ����üũ ����
    if pay!=0:
        while True:
            payment = int(input("��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ� ī��) : "));
            if payment in range(1,3):break;
            else: print("�߸��� �Է��� �Ͽ����ϴ�. �ٽ� �Է��ϼ���."); continue;

        # ������ ���
        if payment == 1:
            inputPay = int(input("����� �Է��ϼ��� : "));
            if inputPay<pay:
                print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�"%(pay-inputPay,inputPay));
                continue;
            elif inputPay==pay:
                print("�����մϴ�. Ƽ���� �����մϴ�");
                guestCount+=1;
            elif inputPay>pay:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�"%(inputPay-pay));
                guestCount+=1;
        # ī���� ���
        elif payment == 2:
            print("���� ���� �ſ� ī���� ���, ���� �ݾ��� 10% ����,\n60~65�� ����� �߰� 5% ���ε˴ϴ�.\n");

            if age in range(60,66): creditCardPay = int(pay*0.9*0.95);
            else: creditCardPay = int(pay*0.9);

            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�.\n"%creditCardPay);
            guestCount+=1;
        # ��� ����üũ ��

        # �������� �� ����Ƽ�� ���� üũ ����
        if guestCount % 7 == 0 and freeTicket>0:
            freeTicket-=1;
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. \n���� ���� Ƽ���� �����մϴ�.\n�ܿ� ����Ƽ�� %d��\n\n"%freeTicket);
        if guestCount % 4 == 0 and discountTicket >0:
            discountTicket-=1;
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�.\n���� ȸ�� ���� Ƽ���� �����մϴ�.\n�ܿ� ����Ƽ�� %d��\n\n"%discountTicket);
    print("%d��° �մ�-------------------------------------\n\n\n" %guestCount);
