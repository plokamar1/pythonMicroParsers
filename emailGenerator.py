op = open('emails.txt','w')

for i in range(149999,200001):
    line = "user"+str(i)+"\n"
    op.write(line)

op.close()