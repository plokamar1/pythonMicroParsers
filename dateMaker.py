#A random date ganerator for work
from random import randint

target = open('finish.txt','w')
target.truncate()

i = 0

for i in range(0,1000):
    day = randint(1,28)
    month = randint(1,12)
    year = randint(1950, 1992)
    newL = str(day) + '-' + str(month) + '-' + str(year)+'\n'
    target.write(newL)

target.close()

