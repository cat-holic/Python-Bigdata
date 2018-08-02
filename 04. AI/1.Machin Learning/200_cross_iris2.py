import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

# 붓꽃의 데이터 읽어들이기 --- 1
csv = pd.read_csv('iris.csv')
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기 --- 2
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]
data = csv.ix[:, 0:4]
label = csv.ix[:, 4]
print(data)
print(label)
# 크로스 벨리데이션하기 --- 3.Homenetwork
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각가의 정답률 = ", scores)
print("평균 정답률 = ", scores.mean())
