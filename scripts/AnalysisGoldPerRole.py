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
                    elements = row[0].split(',')
                    for e in range(0, len(elements)):
                        print(str(e) + ': ' + elements[e])
                break
analyze()