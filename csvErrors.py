import csv
import sys
import os


inputFile = ''
data = ''
outputFile = ''
path = os.path.dirname(os.path.realpath(__file__))+"\\"
if len(sys.argv) == 1:
    inputFile = path + input('Please give me the input file with the accounts:\n')
    data = path + input('Please give me the file with the emails you want me to search:\n')
else:
    inputFile = str(sys.argv[1])
    data = str(sys.argv[2])

f= open(inputFile)
n = open(data)
results = open('finish.txt', 'w');
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
