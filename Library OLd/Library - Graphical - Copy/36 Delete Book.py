head=("Create Book")
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

bfile  = open('Books.csv', "rb")
books = csv.reader(bfile)

bookpos=-1
list2=[]
for row in books:
    list2+=[row]
for x in range (len(list2)):
   if str(list2[x][0])==str(bookno):
            bookpos=x
            break
print design3.center(80)

if bookpos!=-1:
    booknum=raw_input('Re-Enter Book Number\t\t :')
    print design3.center(80)

    if booknum==bookno:
        p=raw_input("Enter Admin Password to Delete: ")
        if p==password():
            if list2[bookpos][2]=='n':
                print
                print "\nNOTE: Book Already Issued by Student."
                list=open_student()
                pos=-1
                for x in range (len(list)):
                    if str(list[x][0])==str(list2[bookpos][3]):
                        pos=x
                        break
                list[pos][2]='n'
                list[pos][3]=','
                student_save(list)
                print "\n\t Existing Book Issue Updated with Student-",list[pos][1]
            list2.pop(bookpos)

            book_save(list2)
            print design3.center(80)
            print "Book Successfully Deleted."
        else:
            print "\n\tPassword Do Not Match"
    else:
        print "\n\tBook Number Do Not Match."        
            
        
else:
    print "Book Number Not in Database"

menu_end()
