import csv
from Functions import *
#______________________________________________________________________________________________________________________________________________________________________
design('*',25)
design('Student Record',1)
design('*',25)
#______________________________________________________________________________________________________________________________________________________________________
list=open_student()

design('_',80)
print "ADMIN NO.\t NAME"
design ('_',80)

for i in range(len(list)):
               print ' ',list[i][0],'   |   ',list[i][1],'\n'
#______________________________________________________________________________________________________________________________________________________________________
menu_end()