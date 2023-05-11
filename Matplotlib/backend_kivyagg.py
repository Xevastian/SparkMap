import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
for ax, color in zip([ax1, ax2, ax3, ax4], ['green', 'red', 'yellow', 'blue']):
   plt.setp(ax.spines.values(), color=color)
   ax.plot([8, 3], c=color)
   plt.setp([ax.get_xticklines(), ax.get_yticklines()], color=color)
plt.show()