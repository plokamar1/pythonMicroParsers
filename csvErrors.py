import csv
import sys
import os


inputFile = ''
data = ''
outputFile = ''
path = os.path.dirname(os.path.realpath(__file__))+"\\"
if len(sys.argv) == 1:
    inputFile = path + input('Please give me the input file with the accounts:\n')
    print(inputFile)
    data = path + input('Please give me the file with the emails you want me to search:\n')
    print(data)
else:
    inputFile = str(sys.argv[1])
    data = str(sys.argv[2])

f= open(inputFile)
firstdata = f.readlines()
n = open(data)
newdata = n.readlines()
finished = open('finish.txt','w');
finished.truncate()
for nline in newdata:
    nline = nline.replace('\n','')
    nline = nline.replace('\t', '')
    for fline in firstdata:
        if nline in fline:
            finished.write(fline)

f.close()
n.close()
finished.close()
