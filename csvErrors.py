import sys
import os


inputFile = ''
data = ''
outputFile = ''
path = os.path.dirname(os.path.realpath(__file__))+"\\"
#Clean previous commands in the command line
for i in range(0,10):
    print('\n')
#User gives the input files
if len(sys.argv) == 1:
    inputFile = path + input('Please give me the input file with the accounts:\n')
    data = path + input('\nPlease give me the file with the emails you want me to search:\n')
else:
    inputFile = str(sys.argv[1])
    data = str(sys.argv[2])
#Try opening the files given
try:
    f= open(inputFile)
except IOError:
    print('There is not such file or directory for input file')
try:
    n = open(data)
except IOError:
    print('There is not such file or directory for data file')

results = open('finish.txt', 'w')
accData = f.readlines()
dataArrray = n.readlines()
results.truncate()#clean the file with the results
for dataLine in dataArrray:
    dataLine = dataLine.replace('\n', '')
    dataLine = dataLine.replace('\t', '')
    for accLine in accData:
        if dataLine in accLine:
            results.write(accLine)

f.close()
n.close()
results.close()
