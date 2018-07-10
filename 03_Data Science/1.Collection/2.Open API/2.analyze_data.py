"""
description":
        "org_link":
        "pDate":
        "title"
"""

import json
import re

with open("이명박_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    # json_data_string = json.dumps(json_data_load, indent=4)
    # json_result = json.loads(json_data_string)

error_data = 0
org_dic = {}
org_list = []
print("데이터 분석을 시작합니다")
for li in json_data_load:
    if li['org_link'] is None or li['org_link'] == "":
        print("'org_link'가 없는 기사를 발견했습니다.")
        error_data += 1
    else:
        m = li['org_link'].split('/')
        org_list.append(m[2])

for li in org_list:
    if org_dic.get(li) is None:
        org_dic[li] = 1
    else:
        org_dic[li] += 1

org_dic_list = sorted(org_dic.items(), key=lambda a: a[1], reverse=True)
print("<네이버 검색 빅데이터 분석>")
print("검색어 : 이명박")
print("전체 도메인수 : {0}".format(len(org_dic)))
print("전체 건수 : {0}".format(len(json_data_load)))
print("부정확한 데이터 수 {0}".format(error_data))

print("- 도메인별 뉴스 기사 분석")
for li in org_dic_list:
    print(">> {0} : {1}건".format(li[0], li[1]))
