# Moodle's system has problems and takes too much time to upload big
# masses of users. So in this script we produce a file for every 1000
# account users read from the input file.
import sys
import os

maxOutput = 1000
inputFile = ''
outputFile = ''

#a counter for every 1000 lines
i = 0
#get path of this file
path = os.path.dirname(os.path.realpath(__file__))+"\\"
#User gives the input files
if len(sys.argv) == 1:
    inputFile = path + input('Please give me the input file with the accounts:\n')
else:
    #get arguments
    inputFile = str(sys.argv[1])
#Try opening the files given
try:
    f= open(inputFile)
except IOError:
    print('There is not such file or directory for input file')
#construction of file name
newFile = 'finish'+ str(i) +'-'+ str(i + maxOutput - 1) +'.txt'
try:
    o = open(newFile, 'w')
except IOError:
    print('Problem')

accounts = f.readlines()
#the first line has the fields. So we keep it
#to enter it first in each file
fields = accounts[0]

for acLine in accounts:
    o.write(acLine)
    i+=1
    if i > maxOutput:
        #close last result file
        o.close()
        #create the new file name
        newFile = 'finish'+ str(i) +'-'+ str(i + maxOutput - 1) +'.txt'
        #open it with write privilleges
        o = open(newFile,'w')
        o.write(fields)
        maxOutput += 1000
        

o.close()
f.close()


