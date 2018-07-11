import re
import urllib.request
import random

print("xml수집")

html = urllib.request.urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn").read().decode('euc-kr')
print([random.randint(-1, 1) for n in range(20)])


