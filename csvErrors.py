import csv
f= open('Updatefinal.txt')
firstdata = f.readlines()
n = open('updatedErrors.txt')
newdata = n.readlines()
finished = open('finish.txt','w');
finished.truncate()
for nline in newdata:
    nline = nline.replace('\n','')
    nline = nline.replace('\t','')
    for fline in firstdata:
        if nline in fline:
            finished.write(fline)

f.close()
n.close()
finished.close()

        
