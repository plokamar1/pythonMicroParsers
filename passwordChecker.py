from sys import argv
import random
from random import randint
import codecs
import string

f = open('passwordNew.txt',encoding='utf-8')
data = f.readlines()
target = open('newPasses.txt','w',encoding='utf-8')

d=0
u=0
l=0
s=0
chars= "!@#$^&*()_+}{|[]:'\/\"?><,.~`"
multiple = string.ascii_letters + chars

for line in data:
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    line = line.replace('\t', '')

    while len(line) < 8:
        newChar = random.choice(multiple)
        line = line + newChar

    for i in line:
        if i.isdigit():
            d = d + 1
        elif i.isupper():
            u = u + 1
        elif i.islower():
            l = l + 1
        elif i in chars:
            s = s + 1

    if not d:
        line = line + str(randint(1, 9))
    if not u:
        letter = random.choice(string.ascii_uppercase)
        line = line + letter
    if not l:
        letter = random.choice(string.ascii_lowercase)
        line = line + letter.lower()
    if not s:
        symbol = random.choice(chars)
        line = line + symbol
    while len(line) < 8 :
        newChar = random.choice(multiple)
        line = line + newChar

    d = 0
    u = 0
    l = 0
    s = 0
    line = line + "\n"
    target.write(line)
    
#target.write(line)
target.close()
f.close()
