import csv
import time
from Functions import *
from Tkinter import *

def student(value1):
   adno=value1
   list=open_student()

   pos=-1
   for x in range (len(list)):
      if str(list[x][0])==str(adno):
            return "\n\tMatch Found with Student-",list[x][1]
            pos=x
            break

   bookpos=-1
   if pos==-1:
      return "\n\tMatch Not Found with Admin Number"


#___________________________________________________________________________________________________________________________________________________
top = Tk()
top.title("Book Issue")

ano=Frame(top,)
ano.grid()

L1 = Label(ano, text="Admin Number")
L1.pack( side = LEFT)
E1 = Entry(ano, bd =5)
E1.pack(side = RIGHT)
B1=Button(ano,compound=RIGHT,text="Enter" ,)
B1.grid()
value1=E1.get()


bno=Frame(top,)
bno.grid()

L2 = Label(bno, text="Book Number")
L2.pack( side = LEFT)

E2 = Entry(bno, bd =5,)
E2.pack(side = RIGHT)
value2=E2.get()

print value2

top.mainloop()

#___________________________________________________________________________________________________________________________________________________
   
'''
def bookissue(value1,value2):
   adno=value1
   bookno=value2
   list=open_student()

   pos=-1
   for x in range (len(list)):
      if str(list[x][0])==str(adno):
            print "\n\tMatch Found with Student-",list[x][1]
            pos=x
            break

   bookpos=-1
   if pos==-1:
   print "\n\tMatch Not Found with Admin Number"
   else:
   

   import time
    
   list2=open_book()
    
    for x in range (len(list2)):
       if str(list2[x][0])==str(bookno):
                print "\n\tMatch Found with Book-",list2[x][1]
                bookpos=x
                break
    time=time.strftime("%d-%m-%y %H:%M")
    if bookpos!=-1:
        if list2[bookpos][2]=='y':
            list2[bookpos][2]='n'
            list2[bookpos][3]=adno
            list2[bookpos][4]=time
        else:
            print "\nBook Already Issued"
    else:
        print "\n\tBook Not in Database"
    if pos!=-1 and bookpos!=-1:
        if list[pos][2]=='n':
            list[pos][2]='y'
            list[pos][3]=bookno
            design('_',80)
            print 'Book Issued Succesfully for ',list[pos][1],' on ',time
        else:
            design('_',80)
            print "Sorry. One Book Already Issued by Student."
    
    student_save(list)
    book_save(list2)
   



design('*',25)
design('Book Issue',1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________
adno=raw_input("Enter the Students Admission Number : ")

list=open_student()

pos=-1
for x in range (len(list)):
   if str(list[x][0])==str(adno):
            print "\n\tMatch Found with Student-",list[x][1]
            pos=x
            break

design('_',80)

bookpos=-1
if pos==-1:
    print "\n\tMatch Not Found with Admin Number"
else:
    bookno=raw_input("Enter the Book Number : ")

    import time
    
    list2=open_book()
    
    for x in range (len(list2)):
       if str(list2[x][0])==str(bookno):
                print "\n\tMatch Found with Book-",list2[x][1]
                bookpos=x
                break
    time=time.strftime("%d-%m-%y %H:%M")
    if bookpos!=-1:
        if list2[bookpos][2]=='y':
            list2[bookpos][2]='n'
            list2[bookpos][3]=adno
            list2[bookpos][4]=time
        else:
            print "\nBook Already Issued"
    else:
        print "\n\tBook Not in Database"
    if pos!=-1 and bookpos!=-1:
        if list[pos][2]=='n':
            list[pos][2]='y'
            list[pos][3]=bookno
            design('_',80)
            print 'Book Issued Succesfully for ',list[pos][1],' on ',time
        else:
            design('_',80)
            print "Sorry. One Book Already Issued by Student."
    
    student_save(list)
    book_save(list2)
#___________________________________________________________________________________________________________________________________________________ 
menu_end()
'''
