import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

wine = pd.read_csv("winequality-both.csv", sep=",", header=0)
wine.columns = wine.columns.str.replace(' ', '_')

print(wine.head())

print("변수별 요약통계 표시")
print(wine.describe())

print("\n 유일값 찾기")
print(sorted(wine.quality.unique()))

print("\n빈도찾기")
print(wine.quality.value_counts())

# Display descriptive statistics for quality by wine type
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print("\n" + '=' * 80)
print('7.2.2 그룹화, 히스토그램, t 검정')
red_wine = wine.ix[wine['type'] == 'red', 'quality']
white_wine = wine.ix[wine['type'] == 'white', 'quality']
sns.set_style('dark')
print(sns.distplot(red_wine, norm_hist=True, kde=False, color="red", label="Red wind"))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color="black", label="White wine"))

# sns.axlabel("quality Score", "Density")
plt.xlabel("Quality Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

# Test whether mean quality is different between red and white wines
print("\n와인의 종류에 따라 품질의 차이 검정")
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat : %.3f pvalue: %.4f' % (tstat, pvalue))
