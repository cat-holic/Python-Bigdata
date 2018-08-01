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

print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'],
                        aggfunc='mean', fill_value='NaN', margins=True))
