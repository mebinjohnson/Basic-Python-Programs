import csv
from Functions import *

head=("View Book")
design1='*'*75
design2='*'*25
design3='_'*80
print design2.center(80)
print head.center(80)
print design2.center(80)

bookno=raw_input("Enter the Book Number : ")

print

list2=open_book()
bookpos=-1
for x in range (len(list2)):
   if str(list2[x][0])==str(bookno):
            bookpos=x
            break
print design3.center(80)
if bookpos!=-1:
    print 'Book Number\t\t :',list2[bookpos][0]
    print 'Book Name\t\t :',list2[bookpos][1]

    print 'Book Availability\t :',
    print 'Available' if list2[bookpos][2]=='y' else "Not Available"

    print 'Book Issued by(Adno)\t :',
    print ' ' if list2[bookpos][3]==',' else list2[bookpos][3]

    print 'Book Issued Time-Date\t :',
    print ' ' if list2[bookpos][4]==',' else list2[bookpos][4]
else:
    print "Book Not in Database"

menu_end()
