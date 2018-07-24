import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

churn = pd.read_csv("churn.csv", sep=",", header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]


churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + \
                         churn['intl_charge']
qcut_names = ['1st_quartile', '2nd_quartile','3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix="total_charges")
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())