import csv
from Functions import *
#______________________________________________________________________________________________________________________________________________________________________
design('*',25)
design('Student Record',1)
design('*',25)
#______________________________________________________________________________________________________________________________________________________________________
list=student_class()

design('_',80)
print "ADMIN NO.\t NAME"
design ('_',80)

for i in list:
               print ' ',i.student_no,'   |   ',i.student_name,'\n'
#______________________________________________________________________________________________________________________________________________________________________
menu_end('31 Student Record.py')
