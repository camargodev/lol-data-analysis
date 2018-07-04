import csv

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/lol-data-analysis/'
FILE = PATH + '/sheets/LOL.csv'
GAME_PARTS = ['Early', 'Mid', 'Late']
BK = 11
RK = 18
TIME_INDEX = 0
LEAGUE_INDEX = 0
X_INDEX = 4
Y_INDEX = 5
LEAGUE = "LCK"

def formatxy(fields):
    x = fields[X_INDEX].replace(' ','')
    y = fields[Y_INDEX].replace(']','').replace('"','').replace(' ','')
    time = fields[TIME_INDEX].replace('[','').replace('"','').replace(' ','')
    x = int(int(x)*1024/15000)
    y = int(int(y)*1024/15000)
    return x,y,float(time)

def computeDeaths(team, index, part):
    wFilename = PATH + 'Plots/Death Heatmaps/sheets/' + str(team) + str(part) + LEAGUE + 'Kills.csv'
    with open(wFilename, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(FILE, newline='') as readFile:
            reader = csv.reader(readFile, delimiter='\n', quotechar='"')
            header = True
            counter = 0
            for row in reader:
                if header:
                    header = False
                    writer.writerow(['x,y'])
                else:
                    #print(counter)
                    counter += 1
                    elements = row[0].split(',')
                    league = elements[LEAGUE_INDEX]
                    #print(league)
                    if str(league).replace(' ','') != LEAGUE:
                        continue
                    kills = elements[index]
                    killList = kills.split(';')
                    for kill in killList:
                        fields = kill.split('|')
                        if fields[0].replace(' ','').replace('[','').replace(']',''):
                            x,y,time = formatxy(fields)
                            line = str(x) + ',' + str(y)
                            if (part == 'Early' and time <= 11):
                                writer.writerow([line])
                            elif (part == 'Mid' and time > 11 and time <= 25):
                                writer.writerow([line])
                            elif part == 'Late' and time > 25:
                                writer.writerow([line])

for part in GAME_PARTS:                                
    computeDeaths('Blue', BK, part)
    computeDeaths('Red', RK, part)