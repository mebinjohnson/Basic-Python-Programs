import csv
from Functions import *
import time
#___________________________________________________________________________________________________________________________________________________
design('*',25)
design('Book Deposit')
design('*',25)
design('_',80)
#___________________________________________________________________________________________________________________________________________________

adno=raw_input("Enter the Students Admission Number : ")

list=student_class()


pos=-1
pos=student_search(adno,list)
bookno=0000
if pos==-1:
    print "\n\tMatch Not Found with Admin Number"
else:
   design('_',80)
   bookno=raw_input("Enter the Book Number : ")
design('_',80)

list2=book_class()
#print list2

bookpos=-1
bookpos=book_search(bookno,list2)
design('_',80)

if bookpos!=-1:
   if bookpos.book_no!=pos.student_bookno:
      print "Issued Book Do Not Match"
   else:
      if bookpos.book_avail=='n':
         bookpos.book_avail='y'
         bookpos.book_issue=','
         bookpos.book_time=','
      else:
         print "Book Not Issued"
      if pos.student_issue=='y':
        pos.student_issue='n'
        pos.student_bookno=','
        print 'Book Succesfully Deposited for ',pos.student_name
      else:
        print "No Issued Book Found In Database for ",pos.student_name
else:
   print "No Book in Database with given Book Number"

student_save(list)

book_save(list2)
#___________________________________________________________________________________________________________________________________________________
menu_end('2 Book Deposit.py')

