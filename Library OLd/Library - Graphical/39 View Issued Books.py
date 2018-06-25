from Functions import *
import csv

design('*',25)
design('View Issued Book',1)
design('*',25)

#___________________________________________________________________________________________________________________________________________________
list2=open_book()

design('-',80)
print 'Book Number\tBook Name \t\tBook Issued by(Adno) \tTime-Date'
design('-',80)
for x in range (len(list2)):
    if list2[x][2]=='n':
        name=''
        cnt=0
        for i in list2[x][1]:
            cnt+=1
            name+=i
            if cnt>22:
                break

        print list2[x][0],'\t|\t',name,'  |  ',list2[x][3],'    |    ',list2[x][4]
#___________________________________________________________________________________________________________________________________________________
menu_end()
