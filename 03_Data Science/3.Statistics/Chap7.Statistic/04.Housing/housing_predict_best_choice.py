import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from pandas import DataFrame
from itertools import combinations

# price	lotsize	bedrooms	bathrms	stories	driveway	recroom	fullbase	gashw	airco	garagepl	prefarea
"""
Coefficients:
Intercept           68121.597070
lotsize              7688.947727
bedrooms             1350.897255
bathrms              7198.713363
stories              5692.756664
garagepl             3656.099034
housing_driveway     2329.802557
housing_recroom      1725.895978
housing_fullbase     2602.692406
housing_gashw        2684.531778
housing_airco        5882.820856
housing_prefarea     3972.972714
"""
housing: DataFrame = pd.read_csv("Housing.csv", sep=",", header=0, index_col=0)

housing.columns = [item.lower() for item in housing.columns]
housing["housing_driveway"] = np.where(housing.driveway == 'yes', 1., 0.)
housing["housing_recroom"] = np.where(housing.recroom == 'yes', 1., 0.)
housing["housing_fullbase"] = np.where(housing.fullbase == 'yes', 1., 0.)
housing["housing_gashw"] = np.where(housing.gashw == 'yes', 1., 0.)
housing["housing_airco"] = np.where(housing.airco == 'yes', 1., 0.)
housing["housing_prefarea"] = np.where(housing.prefarea == 'yes', 1., 0.)

del_list = ["driveway", "recroom", "fullbase", "gashw", "airco", "prefarea"]

for key in del_list:
    housing = housing.drop(labels=key, axis=1)

column_list = []
for key in housing.columns[1:]:
    column_list.append(key)

# 가장 정확한 column 리스트 저장용
max_column = []
max_correct_count = 0

min_column = []
min_correct_count = 0
first_chk = True

print(len(column_list))
for column_size in range(2, len(column_list) + 1):
    combin_columns = combinations(column_list, column_size)
    for column_tuple in combin_columns:
        column = []
        for item in column_tuple:
            column.append(item)
        print("컬럼명")
        formula_set = "price ~"
        for column_item in column:
            formula_set += " " + column_item + " +"

        formula_set = formula_set[:len(formula_set) - 2]

        predict_tool = ols(formula_set, data=housing).fit()
        independent_data = housing[housing.columns.difference(housing.drop(column, axis=1).columns)]
        predicted_result: DataFrame = predict_tool.predict(independent_data)
        rounded_predicted_result = [round(item, ndigits=2) for item in predicted_result]
        correct_count = 0

        for idx, predicted_data in enumerate(rounded_predicted_result):
            # print("%d번째 샘플링 데이터 예측 결과: %d, 실제가격 : %d ==> "
            #       % (idx + 1, predicted_data, housing['price'][idx + 1]), end="")
            if (predicted_data >= housing['price'][idx + 1] * 0.9) and \
                    (predicted_data <= housing['price'][idx + 1] * 1.1):
                # print("정답")
                correct_count += 1
            else:
                print()
                # print("오답")

        if first_chk:
            max_correct_count = correct_count
            min_correct_count = correct_count
            first_chk = False
        elif max_correct_count < correct_count:
            max_correct_count = correct_count
            max_column = column
        elif min_correct_count > correct_count:
            min_correct_count = correct_count
            min_column = column

print("<분석 결과 요약>")
print("관측계수 : %d" % len(housing["price"]))
print("예측값 정답 허용 범위: 실제값의 +- 10.0%")
print("=" * 20 + " 정확도 최상 " + "=" * 20)
print("column 변수 : ", end="")
for column in max_column:
    print(column + ",", end="")
print()
print("정답률: {0} / {1} = {2:.2f}%".format(max_correct_count,
                                         len(housing['price']), max_correct_count / len(housing['price'] * 100)))

print("=" * 20 + " 정확도 최하 " + "=" * 20)
print("column 변수 : ", end="")
for column in min_column:
    print(column + ",", end="")
print()
print("정답률: {0} / {1} = {2:.2f}%".format(min_correct_count,
                                         len(housing['price']), min_correct_count / len(housing['price'] * 100)))

# 5% : lotsize,bedrooms,bathrms,stories,garagepl,housing_driveway,housing_fullbase,housing_gashw,housing_prefarea
# 10%(정확도 40%) : lotsize,bathrms,stories,garagepl,housing_fullbase,housing_airco,housing_prefarea,