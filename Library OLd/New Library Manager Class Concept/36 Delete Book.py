head=("Delete Book")
design1='*'*75
design2='*'*25
design3='_'*80


from Functions import *

import csv

print design2.center(80)
print head.center(80)
print design2.center(80)

bookno=raw_input("Enter the Book Number to Be Deleted: ")

print

list2=book_class()


bookpos=-1
cnt=0
for x in list2:
    if x.book_no==str(bookno):
        bookpos=x
        break
    cnt+=1

print design3.center(80)

if bookpos!=-1:
    booknum=raw_input('Re-Enter Book Number\t\t :')
    print design3.center(80)

    if booknum==bookno:
        p=raw_input("Enter Admin Password to Delete: ")
        if p==password():
            if bookpos.book_avail=='n':
                print
                print "\nNOTE: Book Already Issued by Student."
                list=student_class()
                pos=-1
                for x in list:
                    if x.student_no==bookpos.book_issue:
                        pos=x
                        break
                pos.student_issue='n'
                pos.student_bookno=','
                student_save(list)
                print "\n\t Existing Book Issue Updated with Student-",pos.student_name
            del bookpos
            list2.pop(cnt)

            book_save(list2)
            print design3.center(80)
            print "Book Successfully Deleted."
        else:
            print "\n\tPassword Do Not Match"
    else:
        print "\n\tBook Number Do Not Match."        
            
        
else:
    print "Book Number Not in Database"

menu_end('36 Delete Book.py')
