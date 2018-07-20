# 목적 : 히스토그램(막대그래프) 응용(2개의 막대그래프 그리기

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma * np.random.randn(10000)
x2 = mu2 + sigma * np.random.randn(10000)

fig =plt.figure()
ax1 = fig.add_subplot(1,1,1)
n, bins, patches = ax1.hist(x1, bins=50, normed=False, color="darkgreen")
n, bins, patches = ax1.hist(x2, bins=50, normed=False, color="orange", alpha=0.5)
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position('left')

plt.xlabel("bins")
plt.ylabel('Number of Values in Bin')
fig.suptitle("histograms", fontsize=14, fontweight='bold')
ax1.set_title("Two Frequency Distributions")
fig.savefig('Histogram.png', dpi=400, bbox_inches="tight")
plt.show()
