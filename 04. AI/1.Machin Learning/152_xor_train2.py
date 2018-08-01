import pandas as pd
from sklearn import svm, metrics

# XOR의 계산 결과 데이터
xor_input = [
    # P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- 01
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, :1]  # 데이터
xor_label = xor_df.ix[:, 2]  # 레이블

# 데이터 학습과 예측하기 --- 02
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기 --- 03
ac_scroe = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", ac_scroe)