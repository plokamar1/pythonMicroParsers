from sys import argv

f = open('pyth.txt')
data = f.readlines()
target = open('newPyth.txt','w')

for line in data:
    if len(line) == 10:
        newL = 'I'+line
        target.write(newL)
        newL = 0        
    else:
        newL = str(line).zfill(10)
        newL = 'I'+newL
        target.write(newL)
        newL = 0

target.close()
f.close()
