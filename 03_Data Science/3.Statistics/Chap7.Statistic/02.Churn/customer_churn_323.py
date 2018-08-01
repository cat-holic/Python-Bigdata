import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf


def inverse_logit(model_formula):
    from math import exp
    return (1.0 / (1.0 + exp(-model_formula))) * 100.0


churn = pd.read_csv("churn.csv", sep=",", header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + \
                         churn['intl_charge']

dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

print("\nQuantities you can extract from the result:\n %s" % dir(logit_model))
print("\nCoefficients:\n%s" % logit_model.params)
print("\nCoefficient Std Errors:\n%s" % logit_model)

at_means = float(logit_model.params[0]) + \
           float(logit_model.params[1]) * float(churn['account_length'].mean()) + \
           float(logit_model.params[2]) * float(churn['custserv_calls'].mean()) + \
           float(logit_model.params[3]) * float(churn['total_charges'].mean())

print(churn['account_length'].mean())
print(churn['custserv_calls'].mean())
print(churn['total_charges'].mean())
print(at_means)
print("Probability of churn when independent variables are at their mean values: %.2f"%inverse_logit(at_means))
