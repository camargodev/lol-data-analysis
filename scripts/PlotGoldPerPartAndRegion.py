import csv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/lol-data-analysis/Plots/Gold Per Part/'
REGIONS = ['NALCS', 'EULCS', 'CBLoL', 'LCK']
#X = [i for i in range(1,3+1)]
X = ['Early Game', 'Mid Game', 'Late Game']
Y = [[0 for j in range(len(REGIONS))]for i in range(3)]

def plot():
    #ax = plt.subplot(1, 1, 1)
    #ax.set_title(str(REGIONS[index]))
    NALCS, = plt.plot(X, column(Y,0), 'o-', label='NALCS')
    EULCS, = plt.plot(X, column(Y,1), 'o-', label='EULCS')
    CBLoL, = plt.plot(X, column(Y,2), 'o-', label='CBLoL')
    LCK, = plt.plot(X, column(Y,3), 'o-', label='LCK')
    #plt.axis([1, 3, 0, 1])
    plt.legend([LCK,EULCS,NALCS,CBLoL],['Coreia do Sul','Europa', 'América do Norte', 'Brasil'])
    #plt.legend(CBLoL, ["CBLoL"])
    plt.ylabel('Porcentagem de vitória')
    plt.xlabel('Partes do Jogo')
    fig = plt.gcf()
    fig.savefig(PATH + 'WinRateWithGoldLeadByPartsCBLoLvsLCK.jpg')

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
            if counter == 3:
                counter = 0
        header = False

plt.title('Porcentagem de vitória estando com\nvantagem de ouro nas partes do jogo')
#for i in range(0,len(REGIONS)):
plot()
plt.show()
