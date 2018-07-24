import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# Read the data set into a pandas DataFrame

wine = pd.read_csv("winequality-both.csv", sep=",", header=0)
wine.columns = wine.columns.str.replace(' ', '_')

print(wine.head())

print("변수별 요약통계 표시")
print(wine.describe())

print("\n 유일값 찾기")
print(sorted(wine.quality.unique()))

print("\n빈도찾기")
print(wine.quality.value_counts())