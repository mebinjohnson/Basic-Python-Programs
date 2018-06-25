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

list=open_student()

pos=-1
for x in range (len(list)):
   if str(list[x][0])==str(adno):
            print  "\n\tMatch Found with Student-",list[x][1]
            pos=x
            break
if pos==-1:
    print "\n\tMatch Not Found with Admin Number"
design('_',80)
bookno=raw_input("Enter the Book Number : ")


list2=open_book()

bookpos=-1
for x in range (len(list2)):
   if str(list2[x][0])==str(bookno):
            print "\n\tMatch Found with Book-",list2[x][1]
            bookpos=x
            break
design('_',80)
if bookpos!=-1:
   if list2[bookpos][3]!=list[pos][0]:
      print "Issued Book Do Not Match"
   else:
      if list2[bookpos][2]=='n':
         list2[bookpos][2]='y'
         list2[bookpos][3]=','
         list2[bookpos][4]=','
      else:
         print "Book Not Issued"
      if list[pos][2]=='y':
        list[pos][2]='n'
        list[pos][3]=','
        print 'Book Succesfully Deposited for ',list[pos][1]
      else:
        print "No Issued Book Found In Database for ",list[pos][1]
else:
   print "No Book in Database with given Book Number"

student_save(list)

book_save(list2)
#___________________________________________________________________________________________________________________________________________________
menu_end()

