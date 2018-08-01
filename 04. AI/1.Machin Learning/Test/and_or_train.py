import pandas as pd
from sklearn import svm, metrics

# AND의 계산 결과 데이터
and_input = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]
or_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- 01
and_dataframe = pd.DataFrame(and_input)
or_dataframe = pd.DataFrame(or_input)
and_data = and_dataframe.ix[:, :1]
and_label = and_dataframe.ix[:, 2]

or_data = or_dataframe.ix[:, :1]
or_label = or_dataframe.ix[:, 2]
print(and_data)
print(and_label)

# and 연산 검증
clf = svm.SVC()
clf.fit(and_data, and_label)
pre = clf.predict(and_data)
print(and_label)
print(pre)
ac_score = metrics.accuracy_score(and_label, pre)
print("정확도 : %0.2f" % (ac_score * 100))

# or 연산 검증
clf = svm.SVC()
clf.fit(or_data, or_label)
pre = clf.predict(or_data)
print(or_label)
print(pre)
ac_score = metrics.accuracy_score(or_label, pre)
print("정확도 : %0.2f" % (ac_score * 100))



print(or_label)
# xor_df = pd.DataFrame(xor_input)
# xor_data = xor_df.ix[:, :1]  # 데이터
# xor_label = xor_df.ix[:, 2]  # 레이블
#
# # 데이터 학습과 예측하기 --- 02
# clf = svm.SVC()
# clf.fit(xor_data, xor_label)
# pre = clf.predict(xor_data)
#
# # 정답률 구하기 --- 03
# ac_scroe = metrics.accuracy_score(xor_label, pre)
# print("정답률 = ", ac_scroe)
