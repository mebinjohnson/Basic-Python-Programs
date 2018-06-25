head=("View Student Record")
design1='*'*75
design2='*'*25
design3='_'*80

import csv
from Functions import *

print design2.center(80)
print head.center(80)
print design2.center(80)

adno=raw_input("Enter the Admssion Number of Student : ")

print design3.center(80)

list=open_student()

pos=-1
for x in range (len(list)):
   if str(list[x][0])==str(adno):
            pos=x
            break
print pos
bookno=list[pos][3]
print bookno
list2=open_book()

bookpos=-1
for x in range (len(list2)):
   if str(list2[x][0])==str(bookno):
            bookpos=x
            break
print bookpos
if pos!=-1:
    print 'Admin Number\t\t :',list[pos][0]
    print 'Name of Student\t\t :',list[pos][1]
    print 'Grade\t\t\t :',list[pos][4]
    print 'Section\t\t\t :',list[pos][5]
    print  'House\t\t\t :',list[pos][6]
    print 'Issued Book Number\t :',
    print 'Null' if list[pos][3]==',' else list[pos][3]

    print 'Issued Book\t\t :',
    print 'None ' if list2[bookpos][2]=='y' else list2[bookpos][1]

    print 'Book Issued Time-Date\t :',
    print 'Null ' if list2[bookpos][4]==',' else list2[bookpos][4]
else:
    print "\tStudent Not in Database"


menu_end()

