import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# sepal.length	sepal.width	petal.length	petal.width	variety
# 5.1	3.5	1.4	0.2	Setosa
# 7	    3.2	4.7	1.4	Versicolor

print("빅데이터 로드중..")
iris = pd.read_csv("iris.csv", header=0, sep=",")
print("분석용 빅데이터 가공중..")
iris.columns = [head.lower() for head in iris.columns.str.replace('.', '_')]

iris["irischk"] = np.where(iris['variety'] == 'Setosa', 1., 0.)

dependent_value = iris["irischk"]
independent_value = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
independent_value_with_constant = sm.add_constant(independent_value, prepend=True)

logit_model = sm.Logit(dependent_value, independent_value_with_constant).fit_regularized()

print("샘플링 데이터 예측 테스트 중")
print("20개의 샘플링 데이터 리스트")
sample_data = iris.ix[iris.index.isin(range(40, 60)), independent_value.columns]
sample_data_with_constant = sm.add_constant(sample_data, prepend=True)

predict_data = logit_model.predict(sample_data_with_constant)
rounded_predict_data = [round(item, 2) for item in predict_data]
print("예측결과 분석 중")

correct_chekc = 0
for idx, item in enumerate(rounded_predict_data):
    print("{0}번째 샘플링 데이터 예측결과".format(idx + 1), end=" ")
    if item == 1.:
        print("{0} : Setosa 확실 ==>".format(item), end=" ")
        if item == iris['irischk'][range(40, 60)[idx]]:
            print("정답")
            correct_chekc += 1
        else:
            print("틀림")
    else:
        print("{0} : Setosa 아닌 다른 품종 =>", end=" ")
        if item == iris['irischk'][range(40, 60)[idx]]:
            print("정답")
            correct_chekc += 1
        else:
            print("틀림")

print("<분석결과 요약>")
print("분석계수 : %d" % len(range(40, 60)))
print("정답률 : %d / %d = %.2f%%" % (correct_chekc, len(range(40, 60)), correct_chekc / len(range(40, 60)) * 100))
