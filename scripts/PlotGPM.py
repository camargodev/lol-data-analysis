import csv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/Plots/Gold Per Minute/'
X = [i for i in range(1,101)]
Y = [0 for i in range(1,101)]

with open(PATH + 'Gold.csv', newline='') as readFile:
    reader = csv.reader(readFile, delimiter='\n', quotechar='"')
    header = True
    counter = 0
    for row in reader:
        if not header:
            elements = row[0].split(',')
            Y[counter] = float(elements[1])
            counter = counter + 1
        header = False

plt.plot(X, Y, 'o-')
plt.title('Porcentagem de vitoria estando com\nvantagem de ouro ao decorrer da partida')
plt.axis([1, 100, 0, 1])
plt.ylabel('Y = Porcentagem de vitoria no momento X')
plt.xlabel('X = Decorrer da partida')
fig = plt.gcf()
fig.savefig(PATH + 'WinRateWithGoldLead.jpg')
plt.show()