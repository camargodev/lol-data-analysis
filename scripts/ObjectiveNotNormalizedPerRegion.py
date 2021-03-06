import csv

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/lol-data-analysis'
FILE = PATH + '/sheets/LOL.csv'

REGION_INDEX = 0
WINNER_INDEX = 5

B_INFO = 12
R_INFO = 19
TOWER = 0
INHIB = 1
DRAGON = 2
BARON = 3
HERALD = 4

B_TOWERS = B_INFO + TOWER
B_INHIBS = B_INFO + INHIB
B_DRAGONS = B_INFO + DRAGON
B_BARONS = B_INFO + BARON
B_HERALDS = B_INFO + HERALD

R_TOWERS = R_INFO + TOWER
R_INHIBS = R_INFO + INHIB
R_DRAGONS = R_INFO + DRAGON
R_BARONS = R_INFO + BARON
R_HERALDS = R_INFO + HERALD

REGIONS = ['NALCS', 'EULCS', 'CBLoL', 'LCK']
M = [[0 for j in range(3)]for i in range(len(REGIONS))]

def region_index(region):
    region = region.replace(' ','')
    for i in range(0, len(REGIONS)):
        r = REGIONS[i]
        if region == r:
            return i
    return -1

def counter(objs):
    objs = objs.replace('[','').replace(']','').replace(' ','')
    objs_list = objs.split(';')
    if objs_list[0] == '':
        return 0
    return len(objs_list)
    
def dominant(blues, reds):
    len_blues = counter(blues)
    len_reds = counter(reds)
    if len_blues > len_reds:
        return 1
    else:
        return 0
    
def analyze():
    with open(PATH + '/Plots/Objectives/DominanceNNPerRegion.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        brk = False
        with open(FILE, newline='') as readFile:
            reader = csv.reader(readFile, delimiter='\n', quotechar='"')
            header = True
            for row in reader:
                if header:
                    header = False
                    writer.writerow(['region,towerdom,inhibdom,barondom,dragdom,heralddom'])
                else:
                    elements = row[0].split(',')
                    winner = int(elements[WINNER_INDEX])
                    regionIndex = region_index(elements[REGION_INDEX])
                    if regionIndex >= 0:
                        M[regionIndex][0] += 1
                        
                        M[regionIndex][1] += counter(elements[B_BARONS]) if  winner == 1 else counter(elements[R_BARONS])
                        M[regionIndex][2] += counter(elements[R_BARONS]) if  winner == 1 else counter(elements[B_BARONS])
                        
            for i in range(len(REGIONS)):
                region = REGIONS[i]
                line = region
                line += ',' + str(M[i][1]/M[i][0])
                line += ',' + str(M[i][2]/M[i][0])
                writer.writerow([line])
        print(M)
analyze()
#print(counter("[]"))
#print(counter("[1;2]"))
#print(counter("[1]"))