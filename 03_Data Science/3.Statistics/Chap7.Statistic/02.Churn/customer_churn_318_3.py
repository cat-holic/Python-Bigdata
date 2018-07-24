import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

churn = pd.read_csv("churn.csv", sep=",", header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ', '_').str.replace("\\", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + \
                         churn['intl_charge']
print(churn['total_charges'])

factor_cut = pd.cut(churn.total_charges, 5, precision=2)

print("\n\nfactor_cut \n" + "=" * 80)
print(factor_cut)
print("=" * 80)


def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean(),
            'std': group.std()}


grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())

