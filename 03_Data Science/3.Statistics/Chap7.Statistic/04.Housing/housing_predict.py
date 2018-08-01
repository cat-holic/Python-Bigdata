import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from pandas import DataFrame
from itertools import permutations

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

# print(housing)
formula_set = "price ~ lotsize + bedrooms + bathrms + stories + housing_driveway + housing_recroom +" \
              "housing_fullbase + housing_gashw + housing_airco + housing_prefarea + garagepl"
# housing.drop(["price", "lotsize", "bedrooms", "bathrms", "stories", "driveway", "housing_recroom",
#               "fullbase", "gashw", "airco", "prefarea"], axis=1)
result = ols(formula_set, data=housing).fit()
print(housing.columns)

print(result.params)
dependent_data: DataFrame = housing['price']
independent_data: DataFrame = housing[housing.columns.difference(["price", "driveway", "recroom",
                                                                  "fullbase", "gashw", "airco", "prefarea"])][:10]
# print(independent_data)

predict_result = result.predict(independent_data)
rounded_predict_result = [round(item, ndigits=2) for item in predict_result]
correct_count = 0
for idx, predict_result_data in enumerate(rounded_predict_result):
    print("%d번째 샘플링 데이터 예측 결과: %d, 실제가격 : %d ==> "
          % (idx + 1, predict_result_data, housing['price'][idx + 1]), end="")
    if (predict_result_data >= housing['price'][idx + 1] * 0.95) and \
            (predict_result_data <= housing['price'][idx + 1] * 1.05):
        print("정답")
        correct_count += 1
    else:
        print("오답")

print("<분석 결과 요약>")
print("관측계수: %d" % len(rounded_predict_result))
print("예측값 허용범위 : 실제값의 +- 20%")
print("정답률 %.1f" % (correct_count / len(rounded_predict_result) * 100))
