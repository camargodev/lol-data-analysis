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
M = [[0 for j in range(1+3*5)]for i in range(len(REGIONS))]

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
    
def analyze():
    with open(PATH + '/Plots/Objectives/PerRegion.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        brk = False
        with open(FILE, newline='') as readFile:
            reader = csv.reader(readFile, delimiter='\n', quotechar='"')
            header = True
            for row in reader:
                if header:
                    header = False
                    writer.writerow(['region,wtowers,ltowers,winhibs,linhibs,wbarons,lbarons,wdrags,ldrags,wheralds,lheralds'])
                else:
                    elements = row[0].split(',')
                    winner = int(elements[WINNER_INDEX])
                    regionIndex = region_index(elements[REGION_INDEX])
                    if regionIndex >= 0:
                        M[regionIndex][0] += 1
                        
                        M[regionIndex][1] += counter(elements[B_TOWERS]) + counter(elements[R_TOWERS])
                        M[regionIndex][2] += winner*counter(elements[B_TOWERS]) + (1-winner)*counter(elements[R_TOWERS])
                        M[regionIndex][3] += (1-winner)*counter(elements[B_TOWERS]) + winner*counter(elements[R_TOWERS])
                        
                        M[regionIndex][4] += counter(elements[B_INHIBS]) + counter(elements[R_INHIBS])
                        M[regionIndex][5] += winner*counter(elements[B_INHIBS]) + (1-winner)*counter(elements[R_INHIBS])
                        M[regionIndex][6] += (1-winner)*counter(elements[B_INHIBS]) + winner*counter(elements[R_INHIBS])
                        
                        M[regionIndex][7] += counter(elements[B_BARONS]) + counter(elements[R_BARONS])
                        M[regionIndex][8] += winner*counter(elements[B_BARONS]) + (1-winner)*counter(elements[R_BARONS])
                        M[regionIndex][9] += (1-winner)*counter(elements[B_BARONS]) + winner*counter(elements[R_BARONS])
                        
                        M[regionIndex][10] += counter(elements[B_DRAGONS]) + counter(elements[R_DRAGONS])
                        M[regionIndex][11] += winner*counter(elements[B_DRAGONS]) + (1-winner)*counter(elements[R_DRAGONS])
                        M[regionIndex][12] += (1-winner)*counter(elements[B_DRAGONS]) + winner*counter(elements[R_DRAGONS])
                        
                        #print(elements[R_HERALDS])
                        #print(elements[B_HERALDS])
                        M[regionIndex][13] += counter(elements[B_HERALDS]) + counter(elements[R_HERALDS])
                        M[regionIndex][14] += winner*counter(elements[B_HERALDS]) + (1-winner)*counter(elements[R_HERALDS])
                        M[regionIndex][15] += (1-winner)*counter(elements[B_HERALDS]) + winner*counter(elements[R_HERALDS])
                        #break
                        
        for i in range(len(REGIONS)):
            region = REGIONS[i]
            line = region + ','
            line += str(100*M[i][2]/M[i][1]) + ',' # towers winner
            line += str(100*M[i][3]/M[i][1]) + ',' # towers loser
            line += str(100*M[i][5]/M[i][4]) + ',' # inhibs winner
            line += str(100*M[i][6]/M[i][4]) + ',' # inhibs loser
            line += str(100*M[i][8]/M[i][7]) + ',' # barons winner
            line += str(100*M[i][9]/M[i][7]) + ',' # barons loser
            line += str(100*M[i][11]/M[i][10]) + ',' # drags winner
            line += str(100*M[i][12]/M[i][10]) + ',' # drags loser
            line += str(100*M[i][14]/M[i][13]) + ',' # heralds winner
            line += str(100*M[i][15]/M[i][13]) # heralds loser
            #for j in range(1, 15+1):
            #    line += ',' + str(M[i][j]/M[i][0])
            # print("\nRegião: " + REGIONS[i])
            # print("Média de torres/jogo: " + str(M[i][1]/M[i][0]))
            # print("Média de torres/jogo do vencedor: " + str(M[i][2]/M[i][0]))
            # print("Média de torres/jogo do perdedor: " + str(M[i][3]/M[i][0]))
            # print("Média de inhibs/jogo: " + str(M[i][4]/M[i][0]))
            # print("Média de inhibs/jogo do vencedor: " + str(M[i][5]/M[i][0]))
            # print("Média de inhibs/jogo do perdedor: " + str(M[i][6]/M[i][0]))
            # print("Média de barons/jogo: " + str(M[i][7]/M[i][0]))
            # print("Média de barons/jogo do vencedor: " + str(M[i][8]/M[i][0]))
            # print("Média de barons/jogo do perdedor: " + str(M[i][9]/M[i][0]))
            # print("Média de drags/jogo: " + str(M[i][10]/M[i][0]))
            # print("Média de drags/jogo do vencedor: " + str(M[i][11]/M[i][0]))
            # print("Média de drags/jogo do perdedor: " + str(M[i][12]/M[i][0]))
            # print("Média de heralds/jogo: " + str(M[i][13]/M[i][0]))
            # print("Média de heralds/jogo do vencedor: " + str(M[i][14]/M[i][0]))
            # print("Média de heralds/jogo do perdedor: " + str(M[i][15]/M[i][0]))
            writer.writerow([line])
        print(M)
analyze()
#print(counter("[]"))
#print(counter("[1;2]"))
#print(counter("[1]"))