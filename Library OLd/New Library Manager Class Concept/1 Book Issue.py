import csv
import time
from Functions import *
#___________________________________________________________________________________________________________________________________________________
design('*',25)
design('Book Issue',1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________
adno=raw_input("Enter the Students Admission Number : ")

list=student_class()
pos=-1
pos=student_search(adno,list)

design('_',80)


if pos==-1:
    print "\n\tMatch Not Found with Admin Number"
else:
    bookno=raw_input("Enter the Book Number : ")

    import time
    bookpos=-1
    
    list2=book_class()
    bookpos=book_search(bookno,list2)
   
    time=time.strftime("%d-%m-%y %H:%M")
    if bookpos!=-1:
        if bookpos.book_avail=='y':
            bookpos.book_avail='n'
            bookpos.book_issue=adno
            bookpos.book_time=time
        else:
            print "\nBook Already Issued"
    else:
        print "\n\tBook Not in Database"
    if pos!=-1 and bookpos!=-1:
        if pos.student_issue=='n':
            pos.student_issue='y'
            pos.student_bookno=bookno
            design('_',80)
            print 'Book Issued Succesfully for ',pos.student_name,' on ',time
        else:
            design('_',80)
            print "Sorry. One Book Already Issued by Student."
    
    student_save(list)
    book_save(list2)
#___________________________________________________________________________________________________________________________________________________ 
menu_end('1 Book Issue.py')
