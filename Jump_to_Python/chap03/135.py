def print_gugu_dan(start_dan):
    for i in range(start_dan+5, 10):
        for j in range(1, 10):
            print(i * j, end=" ")
        print('')


start_dan = int(input("시작 단 수를 입력하세요(2~10): "))
print_gugu_dan(start_dan)
