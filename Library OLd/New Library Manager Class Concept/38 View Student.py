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

list=student_class()

pos=-1
for x in list:
   if x.student_no==adno:
            pos=x
            break

if pos!=-1:
   bookno=pos.student_bookno
   print bookno
   list2=book_class()
   bookpos=-1
   for x in list2:
      if x.book_no==bookno:
         bookpos=x
         break
   print 'Admin Number\t\t :',pos.student_no
   print 'Name of Student\t\t :',pos.student_name
   print 'Grade\t\t\t :',pos.student_grade
   print 'Section\t\t\t :',pos.student_section
   print  'House\t\t\t :',pos.student_house
   print 'Issued Book Number\t :', 
   print 'Null' if pos.student_bookno==',' else pos.student_bookno

   print 'Issued Book\t\t :',#pos.student_issue,
   print 'None ' if pos.student_bookno==',' else bookpos.book_name
   print 'Book Issued Time-Date\t :',
   print 'Null ' if  pos.student_bookno==',' ==',' else bookpos.book_time
else:
    print "\tStudent Not in Database"


menu_end('38 View Student.py')

