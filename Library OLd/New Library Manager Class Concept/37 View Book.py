from Functions import *

design('*',25)
design('View Book',1)
design('*',25)

print 
list2=[]
list2=book_class()

print "Total Books in Database\t:\t",Books.total_books
print "Available Books\t\t:\t",Books.avail_books
print "Issued _books\t\t:\t",Books.issued_books
print

bookno=raw_input("Enter the Book Number : ")


bookpos=-1
for x in list2:
   if x.book_no==str(bookno):
            bookpos=x
            break
         
design('_',80)

if bookpos!=-1:
    print 'Book Number\t\t :',bookpos.book_no
    print 'Book Name\t\t :',bookpos.book_name

    print 'Book Availability\t :',
    print 'Available' if bookpos.book_avail=='y' else "Not Available"

    print 'Book Issued by(Adno)\t :',
    print ' ' if bookpos.book_issue==',' else bookpos.book_issue

    print 'Book Issued Time-Date\t :',
    print ' ' if bookpos.book_time==',' else bookpos.book_time
else:
    print "Book Not in Database"

menu_end('37 View Book.py')
