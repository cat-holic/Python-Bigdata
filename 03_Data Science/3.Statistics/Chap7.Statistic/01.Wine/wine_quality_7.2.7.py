import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

print("7.2.7 예측하기")

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = "quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide+" \
             "pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity"

lm = ols(my_formula, data=wine).fit()

dependent_variable = wine['quality']

independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]

new_observations = wine.ix[wine.index.isin(range(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
