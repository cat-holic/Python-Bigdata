import json

with open("2017해외방문색 순위.json", 'r', encoding='utf-8-sig') as readfile:
    a = json.load(readfile)

tem = []
for i in a:
    print(i.items())

print(tem)



