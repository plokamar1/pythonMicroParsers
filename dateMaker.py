#A random date ganerator for testing purposes
from random import randint

target = open('finish.txt','w')
target.truncate()

i = 0

for i in range(0,10000):
    day = randint(1,28)
    month = randint(1,12)
    year = randint(1998, 2015)
    newL = str(day) + '-' + str(month) + '-' + str(year)+'\n'
    target.write(newL)

target.close()

