import json

deberg_chk = 1


def setStudentData(student_data, studentID_Num):
    studentID_Num += 1
    name = input("이름 (예: 홍길동) : ") if deberg_chk == 0 else "홍길동"
    age = input("나이 (예: 29) : ") if deberg_chk == 0 else "29"
    address = input(
        "주소 (대구광역시 동구 아양로 135) : ") if deberg_chk == 0 else "대구광역시 동구 아양로 135"
    num_of_course_learned = input(
        "과거 수강 횟수 (예: 1) : ") if deberg_chk == 0 else "1"
    if input("현재 수강 과목이 있습니까? (예: y/n) : ") == "y":
        learning_course_info = []
        while True:
            course_code = input(
                "강의코드 (예: IB171106, OB0104) : ") if deberg_chk == 0 else "IB171106"
            course_name = input(
                "강의명 (예: IOT 빅데이터 실무반) : ") if deberg_chk == 0 else "IOT 빅데이터 실무반"
            teacher = input("강사명 (예: 김현구) : ") if deberg_chk == 0 else "김현구"
            open_date = input(
                "개강일 (예: 2017-11-06) : ") if deberg_chk == 0 else "2017-11-06"
            close_date = input(
                "종강일 (예: 2018-09-05) : ") if deberg_chk == 0 else "2018-09-05"
            learning_course_info.append({
                "course_code": course_code,
                "course_name": course_name,
                "teacher": teacher,
                "open_date": open_date,
                "close_date": close_date
            })
            if input("현재 수강하는 과목이 더 있습니까? (y/n) : ") == "n":
                break
    total_course_info = {
        "learning_course_info": learning_course_info,
        "num_of_course_learned": num_of_course_learned
    }
    student_data.append({
        "student_ID": "ITT{0:03d}".format(studentID_Num),
        "name": name,
        "age": age,
        "address": address,
        "total_course_info": total_course_info
    })

    with open("ITT_Student.json", "w", encoding="utf-8") as insertStudentInfo:
        json.dump(student_data, insertStudentInfo, indent=4,
                  ensure_ascii=False, sort_keys=True)


def read_json(filename="ITT_Student.json"):
    try:
        with open(filename, "r", encoding="utf-8") as readfile:
            try:
                student_json_data = json.load(readfile)
            except json.JSONDecodeError:
                print("파일 내용이 없습니다.")
    except FileNotFoundError:
        print("파일을 찾을수 없습니다.")
        input_create_change = input(
            "다음 중 원하시는 실행을 입력하세요.(파일 생성=1, 경로 변경=2) : ")
        if input_create_change == "1":
            with open(filename, "w", encoding="utf-8") as creatFile:
                print("파일을 생성하였습니다.")
                student_json_data = []
        elif input_create_change == "2":
            filename = input("경로를 입력하세요")
            student_json_data = read_json(filename)
    return student_json_data


def print_all_student(student_json_data):
    for item in student_json_data:
        print("* 학생아이디 : " + item["student_ID"])
        print("* 이름 : " + item["name"])
        print("* 나이 : " + item["age"])
        print("* 주소 : " + item["address"])
        print("* 수강정보")
        print("  + 과거 수강 횟수 : " +
              item["total_course_info"]["num_of_course_learned"])
        for course in item["total_course_info"]["learning_course_info"]:
            print("  + 현재 수강 과목")
            print("      강의 코드: " + course["course_code"])
            print("      강의명: " + course["course_name"])
            print("      강사: " + course["teacher"])
            print("      개강일: " + course["open_date"])
            print("      종강일: " + course["close_date"])
        print("\n\n")


def print_search_student_result(student_json_data, search_keyword, search_menu):
    # none_element_chk = True
    check_data = []
    for item in student_json_data:
        tem_item = dict(item)
        if search_keyword in tem_item[search_menu]:
            check_data.append(tem_item)
    if len(check_data) > 1:
        # none_element_chk = False
        print("복수 개의 결과가 검색되었습니다.\n"
              "----- 요약 결과 -----")  # 검색 결과가 2건 이상일 때에는 아래와 같이 요약 정보 리스트만 보여줍니다.
        for item in check_data:
            print(">>학생 ID: {0}, 학생 이름 : {1}".format(item["student_ID"], item["name"]))
    elif len(check_data) == 1:
        # none_element_chk = False
        for item in check_data:
            print("* 학생아이디 : " + item["student_ID"])
            print("* 이름 : " + item["name"])
            print("* 나이 : " + item["age"])
            print("* 주소 : " + item["address"])
            print("* 수강정보")
            print("  + 과거 수강 횟수 : " +
                  item["total_course_info"]["num_of_course_learned"])
            for course in item["total_course_info"]["learning_course_info"]:
                print("  + 현재 수강 과목")
                print("      강의 코드: " + course["course_code"])
                print("      강의명: " + course["course_name"])
                print("      강사: " + course["teacher"])
                print("      개강일: " + course["open_date"])
                print("      종강일: " + course["close_date"])
            print()
    else:
        print("검색 결과가 없습니다.")

def print_search_course_result(student_json_data, search_key, search_menu)

def main():
    student_json_data = read_json()
    studentID_Num = len(student_json_data)
    print("           << JSON기반 학생 정보 관리 프로그램 >>")
    print("1.학생 정보입력\n" +
          "2.학생 정보조회\n" +
          "3.학생 정보수정\n" +
          "4.학생 정보삭제\n" +
          "5.프로그램 종료")
    menu_input = input("메뉴를 선택하세요 : ")
    if menu_input == "1":
        setStudentData(student_json_data, studentID_Num)
    elif menu_input == "2":
        print("아래 메뉴를 선택하세요\n"
              "1.전체학생조회\n"
              "2.ID 검색\n"
              "3.이름 검색\n"
              "4.나이 검색\n"
              "5.주소 검색\n"
              "6.과거 수강 횟수 검색\n"
              "7.현재 강의를 수강중인 학생\n"
              "8.현재 수강중인 강의명\n"
              "9.현재 수강 강사\n"
              "10.이전 메뉴")
        find_menu_input = input("메뉴를 선택하세요: ")
        if find_menu_input == "1":
            print_all_student(student_json_data)
            # for item in student_json_data:
            #     print("* 학생아이디 : " + item["student_ID"])
            #     print("* 이름 : " + item["name"])
            #     print("* 나이 : " + item["age"])
            #     print("* 주소 : " + item["address"])
            #     print("* 수강정보")
            #     print("  + 과거 수강 횟수 : " +
            #           item["total_course_info"]["num_of_course_learned"])
            #     for course in item["total_course_info"]["learning_course_info"]:
            #         print("  + 현재 수강 과목")
            #         print("      강의 코드: " + course["course_code"])
            #         print("      강의명: " + course["course_name"])
            #         print("      강사: " + course["teacher"])
            #         print("      개강일: " + course["open_date"])
            #         print("      종강일: " + course["close_date"])
            #     print("\n\n")
        search_keyword = input("검색어를 입력하세요: ").strip()

        if find_menu_input == "2":
            search_menu = "student_ID"
            print_search_student_result(student_json_data, search_keyword, search_menu)
            none_element_chk = True
            for item in student_json_data:
                tem_item = dict(item)
                if tem_item.get("student_ID") == search_keyword:
                    none_element_chk = False
                    print("* 학생아이디 : " + item["student_ID"])
                    print("* 이름 : " + item["name"])
                    print("* 나이 : " + item["age"])
                    print("* 주소 : " + item["address"])
                    print("* 수강정보")
                    print("  + 과거 수강 횟수 : " +
                          item["total_course_info"]["num_of_course_learned"])
                    for course in item["total_course_info"]["learning_course_info"]:
                        print("  + 현재 수강 과목")
                        print("      강의 코드: " + course["course_code"])
                        print("      강의명: " + course["course_name"])
                        print("      강사: " + course["teacher"])
                        print("      개강일: " + course["open_date"])
                        print("      종강일: " + course["close_date"])
            if none_element_chk:
                print("검색 결과가 없습니다.")

        if find_menu_input == "3":
            search_menu = "name"
            print_search_student_result(student_json_data, search_keyword, search_menu)
            # none_element_chk = True
            # for item in student_json_data:
            #     tem_item = dict(item)
            #     check_data = []
            #     if search_keyword in tem_item["name"]:
            #         check_data.append(tem_item)
            # if len(check_data) > 1:
            #     none_element_chk = False
            #     print("복수 개의 결과가 검색되었습니다.\n"
            #           "----- 요약 결과 -----")  # 검색 결과가 2건 이상일 때에는 아래와 같이 요약 정보 리스트만 보여줍니다.
            #     for item in check_data:
            #         print(">>학생 ID: {0}, 학생 이름 : {1}".format(item["student_ID"], item["name"]))
            # elif len(check_data) == 1:
            #     none_element_chk = False
            #     for item in check_data:
            #         print("* 학생아이디 : " + item["student_ID"])
            #         print("* 이름 : " + item["name"])
            #         print("* 나이 : " + item["age"])
            #         print("* 주소 : " + item["address"])
            #         print("* 수강정보")
            #         print("  + 과거 수강 횟수 : " +
            #               item["total_course_info"]["num_of_course_learned"])
            #         for course in item["total_course_info"]["learning_course_info"]:
            #             print("  + 현재 수강 과목")
            #             print("      강의 코드: " + course["course_code"])
            #             print("      강의명: " + course["course_name"])
            #             print("      강사: " + course["teacher"])
            #             print("      개강일: " + course["open_date"])
            #             print("      종강일: " + course["close_date"])
            # else:
            #     print("검색 결과가 없습니다.")

        if find_menu_input == "4":
            search_menu = "age"
            print_search_student_result(student_json_data, search_keyword, search_menu)
            # none_element_chk = True
            # for item in student_json_data:
            #     if item["age"] == search_keyword:
            #         none_element_chk = False
            #         print("* 학생아이디 : " + item["student_ID"])
            #         print("* 이름 : " + item["name"])
            #         print("* 나이 : " + item["age"])
            #         print("* 주소 : " + item["address"])
            #         print("* 수강정보")
            #         print("  + 과거 수강 횟수 : " +
            #               item["total_course_info"]["num_of_course_learned"])
            #         for course in item["total_course_info"]["learning_course_info"]:
            #             print("  + 현재 수강 과목")
            #             print("      강의 코드: " + course["course_code"])
            #             print("      강의명: " + course["course_name"])
            #             print("      강사: " + course["teacher"])
            #             print("      개강일: " + course["open_date"])
            #             print("      종강일: " + course["close_date"])
            #             print()
            # if none_element_chk:
            #     print("검색 결과가 없습니다.")

        if find_menu_input == "5":
            search_menu = "address"
            print_search_student_result(student_json_data, search_keyword, search_menu)
            # none_element_chk = True
            # for item in student_json_data:
            #     tem_item = dict(item)
            #     if tem_item.get("age") == search_keyword:
            #         none_element_chk = False
            #         print("* 학생아이디 : " + item["student_ID"])
            #         print("* 이름 : " + item["name"])
            #         print("* 나이 : " + item["age"])
            #         print("* 주소 : " + item["address"])
            #         print("* 수강정보")
            #         print("  + 과거 수강 횟수 : " +
            #               item["total_course_info"]["num_of_course_learned"])
            #         for course in item["total_course_info"]["learning_course_info"]:
            #             print("  + 현재 수강 과목")
            #             print("      강의 코드: " + course["course_code"])
            #             print("      강의명: " + course["course_name"])
            #             print("      강사: " + course["teacher"])
            #             print("      개강일: " + course["open_date"])
            #             print("      종강일: " + course["close_date"])
            # if none_element_chk:
            #     print("검색 결과가 없습니다.")
        if find_menu_input == "6":
            search_menu = "num_of_course_learned"
            print_search_student_result(student_json_data, search_keyword, search_menu)


if __name__ == "__main__":
    main()
