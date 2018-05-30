import csv

PATH = 'C:/Users/camar/Desktop/UFRGS/T31/'
ORIGINAL = PATH + '/sheets/LeagueofLegends.csv'
FILE = PATH + '/sheets/LOL.csv'

def formatField(element, useSubElements):
    for j in range(0,9):
        element = element.replace(';['+str(j),'|['+str(j))
    subElements = element.split('|')
    formatElement = ''
    for k in range(0, len(subElements)):
        chars = list(subElements[k])
        subElements[k] = subElements[k].replace('[[','[').replace(']]',']')
        if useSubElements:
            chars[0] = ''
            if chars[1] == '[':
                chars[1] = ''
            chars[len(chars)-1] = ''
            if chars[len(chars)-2] == '[':
                chars[len(chars)-2] = ''
            subListStartIndex = chars.index('[')
            subListFinalIndex = chars.index(']')
            for a in range(subListStartIndex, subListFinalIndex):
                if chars[a] == ';':
                    chars[a] = '&'
            chars[0] = '['
            if chars[1] == '':
                chars[1] = '['
            chars[len(chars)-1] = ']'
            if chars[len(chars)-2] == '':
                chars[len(chars)-2] = ']'
            subElements[k] = ''.join(chars)
        formatElement = formatElement + subElements[k] + '|'
    formatElement = formatElement.replace('|','?')
    formatElement = formatElement.replace(';','|')
    formatElement = formatElement.replace('?',';')
    return formatElement[:-1]

with open(FILE, 'w', newline='') as writeFile:
    writer = csv.writer(writeFile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open(ORIGINAL, newline='') as readFile:
        reader = csv.reader(readFile, delimiter='\n', quotechar='"')
        counter = 0
        for row in reader:
            elements = row[0].split(',')
            if counter == 0:
                writer.writerow(row)
                counter = counter + 1
            else:
                newRow = [elements[0]]
                for i in range(1, len(elements)):
                    element = elements[i]
                    if i >= 11 and i <= 23 and i != 17:
                        useSubElements = (i==11 or i==18) and element != '[]'
                        element = formatField(element, useSubElements)
                    newRow = newRow + [','] + [element]
                writer.writerow(newRow)