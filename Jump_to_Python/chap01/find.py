# coding: cp949

a="hobby"

print("find와 index함수의 차이점 비교")

print(a.find('y'))
print("a.find('y') 수행완료")
if a.find('c'):
    print("원하는 결과값이 없음")
print("a.find('c') 수행완료")
print(a.index('y'))
print("a.index('y') 수행완료")
try:
    print(a.index('c'))
    print("a.index('c') 수행완료")
except ValueError as e:
    print("원하는 결과값이 없음")
    print(e)
finally:
    print("c.index('c') 수행완료")
print("\n 12라인 수행으로 13라인 이후는 미출력")
