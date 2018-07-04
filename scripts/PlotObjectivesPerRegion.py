import numpy as np
import matplotlib.pyplot as plt


N = 5

LCK_winners = (7.732, 9.211, 8.193, 7.06, 6.628)
LCK_losers = (2.268, 0.789, 1.807, 2.94, 3.372)

CBLoL_winners = (7.364, 8.785, 7.707, 6.8, 6.538)
CBLoL_losers = (2.636, 1.215, 2.293, 3.2, 3.462)

ind = np.arange(N)    # the x locations for the groups
width = 0.3       # the width of the bars: can also be len(x) sequence
opacity = 0.85
low_opacity = 0.25

p1 = plt.bar(ind, LCK_winners, width, alpha=opacity, color='r')
p2 = plt.bar(ind, LCK_losers, width, bottom=LCK_winners, alpha=low_opacity, color='r')
p3 = plt.bar(ind+width+0.05, CBLoL_winners, width, alpha=opacity, color='g')
p4 = plt.bar(ind+width+0.05, CBLoL_losers, width, bottom=CBLoL_winners, alpha=low_opacity, color='g')

x_axis = [0.2, 1.2, 2.2, 3.2, 4.2]

plt.ylabel('% of objective domination')
plt.title('Win rate for each objective')
plt.xticks(x_axis, ('Towers', 'Inhibitors', 'Barons', 'Dragons', 'Heralds'))
plt.yticks(np.arange(0, 10+1, 1))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('LCK winning teams',
'LCK losing teams', 'CBLoL winning teams',
'CBLoL losing teams'), loc=2, borderaxespad=0.,
bbox_to_anchor=(1.05, 1))

plt.show()