from bs4 import BeautifulSoup
import urllib.request
from pandas import DataFrame
import json
import os

file_index = 1
folder_index = 1


def make_dir(file_mode=True, cvs_mode=True):
    folder_name = "naver-ranking"
    cvs_file_name = "movie"
    index_file_name = "data_index.json"
    global folder_index
    global file_index
    if file_mode:
        file_dir = folder_name + str(folder_index) + "/"
        if cvs_mode:
            file_dir += cvs_file_name + str(file_index) + ".cvs"
            return file_dir
        if not cvs_mode:
            file_dir += index_file_name
            return file_dir
    elif not file_mode:
        folder_dir = folder_name + str(folder_index) + "/"
        return folder_dir


def get_index_dic():
    global folder_index
    # 첫번째 폴더가 있을 경우
    if os.path.exists(make_dir(file_mode=False)):
        print("첫번째 폴더 존재")
        # 폴더내에 index 파일 찾기 로직
        while True:
            if os.path.exists(make_dir(cvs_mode=False)):
                print("data_index 파일이 {0}에서 발견되었습니다.".format(make_dir(cvs_mode=False)))
                with open(make_dir(cvs_mode=False), mode="r",
                          encoding="UTF-8") as openIndex:
                    index_of_file = json.load(openIndex)
                    return index_of_file
            folder_index += 1
    # 첫번째 폴더가 없을 경우 폴더 생성 후 index 파일 생성
    else:
        os.mkdir(make_dir(file_mode=False))
        with open(make_dir(file_mode=True, cvs_mode=False), mode="w",
                  encoding="UTF-8") as createIndex:
            index_of_file = {'file': 0, 'folder': 1}
            json.dump(index_of_file, createIndex, indent=4)
        return index_of_file


def save_file():
    global file_index
    global folder_index
    if not os.path.exists(make_dir(file_mode=False)):
        os.mkdir(make_dir(file_mode=False))
    result_table.to_csv(make_dir(), encoding="utf-8", mode='w', index=False, sep=",")
    print("빅데이터가 파일 경로 : {0}에 저장되었습니다.".format(make_dir()))
    folder_index += 1
    if not os.path.exists(make_dir(cvs_mode=False)):
        os.mkdir(make_dir(file_mode=False))
    with open(make_dir(cvs_mode=False), mode='w', encoding='utf-8') as saveIndex:
        print("인덱스 파일을 저장합니다")
        folder_index -= 1
        index_dic_for_save = {'file': file_index, 'folder': folder_index}
        json.dump(index_dic_for_save, saveIndex)
        print("인덱스 파일이 파일 경로 : {0}에 저장되었습니다.".format(make_dir(cvs_mode=False)))

        if os.path.exists(make_dir(cvs_mode=False)):
            os.remove(make_dir(cvs_mode=False))


print("빅데이터 수집을 시작합니다.")
html = urllib.request.urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
bs = BeautifulSoup(html, 'html.parser')

tag = bs.findAll('div', attrs={'class': 'tit3'})
updown = bs.find_all('img', attrs={'class': 'arrow'})
updown_range = bs.find_all('td', attrs={'class': 'range ac'})
movie_name_list = []

# 영화 이름 리스트 초기화
for movie_name in tag:
    movie_name_list.append(movie_name.text.replace('\n', '').replace(' ', ''))
# 영화 랭크 변동여부 입력
movie_updown_list = []
for item in updown:
    movie_updown_list.append(item.attrs['alt'])
# 영화 랭크 변동크기 입력
movie_updown_range_list = []
for item in updown_range:
    movie_updown_range_list.append(item.text.strip())
result = {'rank': range(1, 51), 'name': movie_name_list, 'range': movie_updown_range_list, 'up_down': movie_updown_list}

result_table = DataFrame(result, columns=['rank', 'name', 'range', 'up_down'], index=result['rank'])
print("빅데이터 수집을 완료하였습니다.")
print("빅데이터를 저장합니다.")

index_dic = get_index_dic()
folder_index = index_dic['folder']
file_index = index_dic['file'] + 1

if file_index > 3:
    folder_index += 1
    file_index = 1

save_file()

# try:
#     with open("/"+folder_name + "/" + data_index_file_name, mode="r", encoding="utf-8") as indexStream:
#         index = json.load(indexStream)
# except FileNotFoundError as e:
#     print("파일이 없습니다. 인덱스 파일을 먼저 생성합니다.")
#     with open(folder_name + str(folder_idx) + "/" + data_index_file_name, mode="w",
#       encoding="utf-8") as create_index_stream:
#         index_dic = {"folder": folder_idx, "file": file_index}
#         json.dump(index_dic, create_index_stream, indent=4, sort_keys=True, ensure_ascii=True)
# result_table.to_csv("naver_rank.csv", encoding="utf-8", mode='w', index=False, sep=",")
# print("저장을 완료하였습니다.")
