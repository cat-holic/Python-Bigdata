import csv


def convert_type(col_instance):
    try:
        col_instance = list(map(int, col_instance))
    except ValueError:
        col_instance = list(map(float, col_instance))
    return col_instance


def print_row(row_instance):
    print("행데이터는 아래와 같습니다")
    for row_element in row_instance:
        print("%s" % row_element, end="")
    print()


def print_col(col_instance):
    for col_element in col_instance:
        print(col_element)


def exit_csv_basic():
    print("프로그램을 종료합니다")


def column(data, accessKey):
    col_instance = []
    indexOfAccessKey = data[0].index(accessKey)

    for li in data[1:]:
        col_instance.append(li[indexOfAccessKey])

    col_instance = list(map(int, col_instance))

    return col_instance


def sum_column(col_instance):
    return sum(col_instance)


def avg_column(col_instance):
    avg = sum(col_instance) / len(col_instance)
    return avg


def max_col(col_instance):
    return max(col_instance)


def min_col(col_instance):
    return min(col_instance)


def deviation_col(col_instance):
    avg = avg_column(col_instance)
    dev_col = []
    for col_element in col_instance:
        dev_col.append(col_element-avg)

    return dev_col


def variance_col(col_instance):
    var_temp = []
    for dev_element in deviation_col(col_instance):
        var_temp.append(dev_element**2)

    var_col = sum(var_temp)/len(var_temp)
    return var_col


def std_dev_col(col_instance):
    std_dev_col_num = variance_col(col_instance)**0.5
    return std_dev_col_num

def asc_col(col_instance):
    col_instance = sorted(col_instance)
    return col_instance

def desc_col(col_instance):
    col_instance = sorted(col_instance,reverse = True)
    return col_instance

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as infile:
    data = list(csv.reader(infile))

while True:
    selectNum = int(input("0.종료 1.행 2.열 3.Homenetwork.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬"
                          "\n메뉴를 선택하세요: "))
    if selectNum == 0:
        exit_csv_basic()
        break
    accessKey = input("Access Key를 입력하세요: ")
    if selectNum == 1:
        row_instance = data[accessKey]
        print_row(row_instance)
        continue

    col_instance = column(data, accessKey)

    if selectNum == 2:
        print_col(col_instance)
    elif selectNum == 3:
        print_col(col_instance)
        print("총합 : %d" % sum_column(col_instance))
    elif selectNum == 4:
        print_col(col_instance)
        print("평균값 {0}".format(avg_column(col_instance)))
    elif selectNum == 5:
        print_col(col_instance)
        print("최대값 : " + max_col(col_instance))
    elif selectNum == 6:
        print_col(col_instance)
        print("최소값 : " + min_col(col_instance))
    elif selectNum == 7:
        print("{0:4}{1}".format("표본", "편차"))
        for li in range(len(col_instance)):
            print("{0:<4}{1:>18}".format(col_instance[li], deviation_col(col_instance)[li]))
    elif selectNum == 8:
        print_col(col_instance)
        print("표준편차 : " + str(std_dev_col(col_instance)))
    elif selectNum == 9:
        print_col(col_instance)
        print("분산 : " + str(variance_col(col_instance)))
    elif selectNum == 10:
        for col_object in asc_col(col_instance):
            print(col_object, end="")
        print()
    elif selectNum == 11:
        for col_object in desc_col(col_instance):
            print(col_object, end="")
        print()