import csv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/Plots/Gold Per Minute/'
REGIONS = ['NALCS', 'EULCS', 'CBLoL', 'LCK']
X = [i for i in range(1,101)]
Y = [[0 for j in range(len(REGIONS))]for i in range(100)]

def plot():
    #ax = plt.subplot(1, 1, 1)
    #ax.set_title(str(REGIONS[index]))
    LCK, = plt.plot(X, column(Y,3), 'o-', label='LCK')
    CBLoL, = plt.plot(X, column(Y,2), 'd-', label='CBLoL')
    plt.axis([1, 100, 0, 1])
    plt.legend([LCK,CBLoL],['LCK','CBLoL'])
    #plt.legend(CBLoL, ["CBLoL"])
    plt.ylabel('Y = Porcentagem de vitoria no momento X')
    plt.xlabel('X = Decorrer da partida')
    fig = plt.gcf()
    fig.savefig(PATH + 'WinRateWithGoldLeadCBLoLvsLCK.jpg')

def column(matrix, i):
    return [row[i] for row in matrix]

def indexRegion(region):
    region = region.replace(' ','')
    for i in range(0, len(REGIONS)):
        r = REGIONS[i]
        if region == r:
            return i
    return -1

with open(PATH + '/GoldByRegion.csv', newline='') as readFile:
    reader = csv.reader(readFile, delimiter='\n', quotechar='"')
    header = True
    counter = 0
    for row in reader:
        if not header:
            elements = row[0].split(',')
            index = indexRegion(elements[0])
            Y[counter][index] = float(elements[2])
            counter = counter + 1
            if counter == 100:
                counter = 0
        header = False

plt.title('Porcentagem de vitoria estando com\nvantagem de ouro ao decorrer da partida')
#for i in range(0,len(REGIONS)):
plot()
plt.show()
