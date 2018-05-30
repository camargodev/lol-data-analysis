import csv

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/'
FILE = PATH + '/sheets/LOL.csv'
GAME_PARTS = ['Early', 'Mid', 'Late']
YEARS = [2014,2015,2016,2017,2018]
TEAMS = ['Blue','Red']
KILL_INDEXES = [11,18]

YEAR_INDEX = 1
TIME_INDEX = 0
X_INDEX = 4
Y_INDEX = 5

def formatxy(fields):
    x = fields[X_INDEX].replace(' ','')
    y = fields[Y_INDEX].replace(']','').replace('"','').replace(' ','')
    time = fields[TIME_INDEX].replace('[','').replace('"','').replace(' ','')
    x = int(int(x)*1024/15000)
    y = int(int(y)*1024/15000)
    return x,y,float(time)
    
def getGamePart(time):
    if time <= 11:
        return 'Early'
    elif time > 11 and time <= 25:
        return 'Mid'
    else:
        return 'Late'
    
def shouldWrite(part, year, fileTime, fileYear):
    if year == int(fileYear):
        filePart = getGamePart(fileTime)
        return part == filePart
    else:
        return False

def computeDeaths(team, index, part, pyear):
    wFilename = PATH + 'Plots/Death Heatmaps/PerYear/sheets/' + str(pyear) + str(team) + str(part) + 'Kills.csv'
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
                    elements = row[0].split(',')
                    year = elements[1]
                    kills = elements[index]
                    killList = kills.split(';')
                    for kill in killList:
                        fields = kill.split('|')
                        if fields[0].replace(' ','').replace('[','').replace(']',''):
                            x,y,time = formatxy(fields)
                            line = str(year) + ',' + str(x) + ',' + str(y)
                            if shouldWrite(part, pyear, time, year):
                                #print(str(counter) + ':' + line)
                                writer.writerow([line])
                            #counter = counter+1


for part in GAME_PARTS:
    for year in YEARS:
        for t in range(0, len(TEAMS)):
            team = TEAMS[t]
            index = KILL_INDEXES[t]
            computeDeaths(team, index, part, year)
            
            
            