import csv

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/'
FILE = PATH + '/sheets/LOL.csv'
GOLD_INDEX = 9
DURATION_INDEX = 8
BWINNER_INDEX = 5

M = [[0 for j in range(2)] for i in range(100)]

def analyze():
    with open(PATH + 'Plots/Gold Per Minute/Gold.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        brk = False
        with open(FILE, newline='') as readFile:
            reader = csv.reader(readFile, delimiter='\n', quotechar='"')
            header = True
            brk = False
            for row in reader:
                if header:
                    header = False
                    writer.writerow(['part,pctofwin'])
                else:
                    elements = row[0].split(',')
                    goldleaders = elements[GOLD_INDEX].replace('[','').replace(']','').split(';')
                    duration = int(elements[DURATION_INDEX]) 
                    winner = int(elements[BWINNER_INDEX])
                    for i in range(0, len(goldleaders)):
                        leader = 1 if int(goldleaders[i]) > 0 else 0
                        moment = int((i+1)*100/duration)
                        M[moment-1][0] = M[moment-1][0] + (1 if leader == winner else 0)
                        M[moment-1][1] = M[moment-1][1] + 1
        for i in range(0,100):
            if M[i][1] == 0:
                M[i][0] = (M[i-1][0] + M[i+1][0])/2
                M[i][1] = (M[i-1][1] + M[i+1][1])/2
            writer.writerow([str(i+1) + ',' + str(M[i][0]/ M[i][1])])
            
analyze()