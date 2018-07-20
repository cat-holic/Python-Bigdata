from numpy.random import randn
import matplotlib.pyplot as plt

plot_data1 = randn(36).cumsum()
plot_data2 = randn(36).cumsum()
plot_data3 = randn(36).cumsum()
plot_data4 = randn(36).cumsum()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='LGE')
ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Samsung E')
ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label="KB")
ax1.plot(plot_data4, marker='s', color='orange', linestyle=':', label='HyundaiH')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Line plot: Markers, Colors, and Linestyles')
plt.xlabel("Draw")
plt.ylabel("Random Number")
plt.legend(loc="best")

plt.savefig('line_plot.png', dpi=400, bbox_inches="tight")
plt.show()