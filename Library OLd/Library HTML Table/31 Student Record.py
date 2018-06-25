import csv
from Functions import *


design('*',25)
design('Student Record',1)
design('*',25)


print

list=open_student()

design('_',80)
print "ADMIN NO.\t NAME"
design ('_',80)

for i in range(len(list)):
               print ' ',list[i][0],'   |   ',list[i][1],'\t\t|\t',list[i][6],'\n'

menu_end()
