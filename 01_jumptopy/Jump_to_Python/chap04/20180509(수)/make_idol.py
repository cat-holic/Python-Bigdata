def show_candidates(candidate_list):
    for i in candidate_list:
        print(i, end=' ')
    print()


def make_idol(candidate_list):
    for i in candidate_list:
        print("신예 아이돌 %s 인기 급상승" % i)


def make_world_star(candidate_list):
    for i in candidate_list:
        print("아이돌 %s 월드스타 등극" % i)


with open("C:/bigdata/Jump_to_Python/chap04/20180509(수)/연습생.txt", 'r', encoding='utf-8') as f:
    idol_list_temp = f.readlines()
    idol_list = []
    for i in idol_list_temp:
        idol_list.append(i.replace('\n', '').replace('\ufeff', ''))


show_candidates(idol_list)
make_idol(idol_list)
make_world_star(idol_list)
