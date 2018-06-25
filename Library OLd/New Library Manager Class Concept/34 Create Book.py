from Functions import *
import time
import csv

design('*',25)
design('Create Book',1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________

bookno=int(input("Enter the Book Number to Be Created: "))

list2=book_class()
bookpos=-1

for x in list2:   
   if int(x.book_no)==bookno:
            bookpos=x
            break

design('_',80)

while bookpos==-1:
   booknum=raw_input('Re-Enter Book Number\t : ')
   if int(booknum)==bookno:
      bookname=raw_input( 'Book Name\t\t : ')
      newdata=Books(booknum,bookname,'y')
      list2.append(newdata)
      book_save(list2)
      print '\n\tNew Book Added to Database'
   else:
      print "\n\tEntered Book Number Do Not Match"
      break
   break    
else:
    print "Book Number Already in Use"

#___________________________________________________________________________________________________________________________________________________
menu_end('34 Create Book.py')
