from bs4 import BeautifulSoup
import urllib.request
from pandas import DataFrame

print("xml수집")
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
result_table.to_csv("naver_rank.csv", encoding="utf-8", mode='w', index=False, sep=",")

# test_table = DataFrame({"rank": "", "name": "", "range": "", "up_down": ""})
#
# print(result_table)
# print("--------------------영화이름 리스트----------------------")
# # print(movie_name_list)
# print("--------------------랭크 리스트----------------------")
# # print(updown)
