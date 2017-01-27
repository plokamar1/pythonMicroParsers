op = open('raw.txt')
target = open('formatedTime.txt','w')
target.truncate()
data = op.readlines()
arStart = '\'\'=>array(\n'
target.write(arStart)

for line in data:
    line = line.replace('\n','')
    newL = '\t\''+ str(line) + '\',\n'
    target.write(newL)

arFin = '),'
target.write(arFin)

op.close()
target.close()
