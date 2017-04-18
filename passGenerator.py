from sys import argv
import random
from random import randint
import codecs
import string
sCharsFlag = False

def standartChars( repeats, sCharsFlag):
    chars = "!@#$^&*()_+}{|[]:'\/\"?><,."
    passesL = []
    passStr = []
    i = 0
    while i < repeats:#we use this one to emulate the repeats for every line

        randUpper = random.choice(string.ascii_uppercase)#find random uppercase
        passStr.append(randUpper)

        if sCharsFlag == True:
            specialC = random.choice(chars)#special characters
            passStr.append(specialC)
        
        randLower = random.choice(string.ascii_lowercase)#find random lowercase
        passStr.append(randLower)
        
        randDig = str(randint(0, 9))#find a random digit
        passStr.append(randDig)

        passesL.append(passStr)
        passStr = []
        i += 1
    return(passesL)

def randomChar(sCharsFlag):
    sChars = "!@#$^&*()_+}{|[]:'\/\"?><,."
    digits = "1234567890"
    chars = string.ascii_letters
    chars += digits
    if sCharsFlag == True :
        chars += sChars
    return(random.choice(chars))


def mainPass():
    choice = input("Would you like to create new passwords(1) or check if existing passwords are made according to the recommended settings(2)?(Type 1 or 2)\n(The recommended settings are: at least 8 characters, at least 1 lowercase, at least 1 uppercase, at least 1 digit and at least 1 special character)\n")

    #Case of creating passwords
    if choice == "1":
    #Repeat the question until getting a valid reply
        while True:
            passNum = input("How many passwords would you like to produce?(Max 100.000)\n")
            if int(passNum) <= 100000 and int(passNum) > 0:
                break
        while True:
            sCharsFlag = input("Would you like special characters?(Type y or n)\n")
            if sCharsFlag == "y":
                sCharsFlag = True
                break
            elif sCharsFlag == "n":
                sCharsFlag = False
                break

    #Get the standart values we need for each line existing in the file
        passesL = standartChars(int(passNum), sCharsFlag)

        created = open('createdPasswords.txt', 'w', encoding = 'utf-8')

        for i in range(0, int(passNum)):
            while len(passesL[i]) < 8:
                char = randomChar(sCharsFlag)
                pos = randint(0, len(passesL[i]))
                if char == "\"" and pos == 0:
                    pos = randint(1,len(passesL[i]))
                passesL[i].insert(pos, char)

            passesL[i].append("\n")
            password = "".join(passesL[i])
            created.write(password)

        created.close()

mainPass()