import numpy as np
import matplotlib.pyplot as plt
import matplotlib


PATH = 'C:/Users/camar/Desktop/UFRGS/T31/lol-data-analysis/Plots/Objectives/'
N = 5

CBLoL= (0.9534883720930233, 0.9302325581395349, 0.740797342192691, 0.7740863787375415, 0.5980066445182725)
LCK = (0.9743944636678201, 0.9584775086505191, 0.8542906574394463, 0.784083044982699, 0.5480968858131487)

ind = np.arange(N)    # the x locations for the groups
width = 0.3       # the width of the bars: can also be len(x) sequence
opacity = 0.75

p1 = plt.bar(ind, LCK, width, alpha=opacity, color='r')
p2 = plt.bar(ind+width+0.05, CBLoL, width, alpha=opacity, color='g')

x_axis = [0.175, 1.175, 2.175, 3.175, 4.175]
plt.subplots_adjust(right=0.75)

plt.ylabel('Porcentagem de dominância')
plt.title('Dominância de objetivos pelo vencedor da partida')
plt.xticks(x_axis, ('Torres', 'Inibidores', 'Barões', 'Dragões', 'Arautos'))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend((p1[0], p2[0]), ('Coreia do Sul', 'Brasil'), loc=2, borderaxespad=0., bbox_to_anchor=(1.01, 1))

fig = plt.gcf()
fig.savefig(PATH + 'DominaneCBLoLxLCK.jpg')
plt.show()