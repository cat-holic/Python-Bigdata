import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Histogram
x= np.random.normal(size=10)
sns.distplot(x, bins=20, kde=True, rug=False, label='Histogram w/o Density')
sns.utils.axlabel('Value', 'Frequency')
plt.title("histogram of a Random sample from a normal Distribution")
plt.legend()
plt.show()