import csv

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/'
FILE = PATH + '/sheets/LOL.csv'
REGION_INDEX = 0
GOLD_INDEX = 9
DURATION_INDEX = 8
BWINNER_INDEX = 5

REGIONS = ['NALCS', 'EULCS', 'CBLoL', 'LCK']
M = [[0 for j in range(2)]for i in range(len(REGIONS)*100)]

def indexRegion(region):
    region = region.replace(' ','')
    for i in range(0, len(REGIONS)):
        r = REGIONS[i]
        if region == r:
            return i
    return -1

def analyze():
    with open(PATH + 'Plots/Gold Per Minute/GoldByRegion.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        brk = False
        with open(FILE, newline='') as readFile:
            reader = csv.reader(readFile, delimiter='\n', quotechar='"')
            header = True
            for row in reader:
                if header:
                    header = False
                    writer.writerow(['region,part,pctofwin'])
                else:
                    elements = row[0].split(',')
                    goldleaders = elements[GOLD_INDEX].replace('[','').replace(']','').split(';')
                    duration = int(elements[DURATION_INDEX]) 
                    winner = int(elements[BWINNER_INDEX])
                    regionIndex = indexRegion(elements[REGION_INDEX])
                    for i in range(0, len(goldleaders)):
                        if regionIndex >= 0:
                            leader = 1 if int(goldleaders[i]) > 0 else 0
                            moment = int((i+1)*100/duration)
                            index = regionIndex*100+moment-1
                            M[index][0] = M[index][0] + (1 if leader == winner else 0)
                            M[index][1] = M[index][1] + 1
                    brk = False
                if brk:
                    break
        for i in range(len(REGIONS)*100):
            if M[i][1] == 0:
                M[i][0] = (M[i-1][0] + M[i+1][0])/2
                M[i][1] = (M[i-1][1] + M[i+1][1])/2
            part = i%100
            region = REGIONS[int((i-part)/100)]
            pct = M[i][0]/ M[i][1]
            line = str(region) + ',' + str(part) + ',' + str(pct)
            writer.writerow([line])
analyze()