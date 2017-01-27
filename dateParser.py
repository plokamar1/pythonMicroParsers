f = open('pyth.txt')
data = f.readlines()
target = open('newPyth.txt','w')
target.truncate()

for line in data:
    line = line.replace('\n','')
    newL = line.split('/')
    newL = str(newL[2]) + '-' + str(newL[1]) + '-' + str(newL[0])+'\n'
    target.write(newL)

target.close()
f.close()
