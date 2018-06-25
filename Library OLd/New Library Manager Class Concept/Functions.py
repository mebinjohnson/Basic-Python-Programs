class Books:
    avail_books=0
    total_books=0
    issued_books=0
    def __init__(self,no,name,avail,issue=',',time=','):
                 self.book_no=no
                 self.book_name=name
                 self.book_avail=avail
                 self.book_issue=issue
                 self.book_time=time
                 Books.book_count(self)
        
    def __str__(self):
                print str(self.book_no),str(self.book_name),str(self.book_avail)
    def book_count(self):
            Books.total_books+=1
            if self.book_avail=='y':
                Books.avail_books+=1
                Books.issued_books=Books.total_books-Books.avail_books

#___________________________________________________________________________________________________________________________________________________

class Student:
    total_students=0
    def __init__(self,no,name,issue,bookno,grade,section,house):
        self.student_no=no
        self.student_name=name
        self.student_issue=issue
        self.student_bookno=bookno
        self.student_grade=grade
        self.student_section=section
        self.student_house=house
        Student.total_students+=1
#___________________________________________________________________________________________________________________________________________________
           
def student_class():
    list=[]
    import csv
    sfile  = open('Student ID.csv', "rb")
    sread= csv.reader(sfile)
    for row in sread:
        t=Student(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        list.append(t)
    return list


#___________________________________________________________________________________________________________________________________________________

def book_class():
    list=[]
    Books.avail_books=0
    Books.total_books=0
    Books.issued_books=0
    import csv
    bfile  = open('Books.csv', "rb")
    books = csv.reader(bfile)
    for row in books:
        s=Books(row[0],row[1],row[2],row[3],row[4])
        s.book_count()
        list.append(s)
    return list

#___________________________________________________________________________________________________________________________________________________

def design(char,no=1):
    design=str(char)*int(no)
    print design.center(80)

#___________________________________________________________________________________________________________________________________________________

def refresh(file):
    execfile( str(file))    

#___________________________________________________________________________________________________________________________________________________  

def menu_end(file_name= "0 Main.py"):
    design3='_'*80
    print design3.center(80)
    print ("Selection:\n\t1. Main Menu \n\t2. Administrator Menu \n\t3. Reload \n\t4. Exit")
    select=raw_input("Enter Selection (1-3) : ")
    import subprocess as sp
    sp.call('cls',shell=True)
    import os
    if select=='4':
        exit()
    if select=='2':
        execfile( "3 Administrator Menu.py")
    if select=='3':
        execfile(str(file_name))
    else:
        execfile( "0 Main.py")

#___________________________________________________________________________________________________________________________________________________
def student_search(num,slist):
    s_pos=-1
    for x in slist:
       if str(x.student_no)==str(num):
           s_pos=x
           print "\n\tMatch Found with : ",s_pos.student_name
           break
    return s_pos
#___________________________________________________________________________________________________________________________________________________

def book_search(num,slist):
    s_pos=-1
    for x in slist:
       if str(x.book_no)==str(num):
           s_pos=x
           print "\n\tMatch Found with : ",s_pos.book_name
           break
    return s_pos
#___________________________________________________________________________________________________________________________________________________    

def book_save(save_list):
    write_list=[]
    for i in save_list:
        write_list+=[[i.book_no,str(i.book_name),str(i.book_avail),str(i.book_issue),str(i.book_time)]]
    import csv
    bofile  = open('Books.csv', "w")
    bwriter = csv.writer(bofile)
    for row in write_list:
        bwriter.writerow(row)
 
#___________________________________________________________________________________________________________________________________________________

def student_save(save_list):
    write_list=[]
    for i in save_list:
        write_list+=[[i.student_no,i.student_name,i.student_issue,i.student_bookno,i.student_grade,i.student_section,i.student_house]]
    import csv
    ofile  = open('Student ID.csv', "wb")
    writer = csv.writer(ofile)
    for row in write_list:
        writer.writerow(row)
#___________________________________________________________________________________________________________________________________________________

def password():
    pfile  = open('Password.dat', "r+")
    passw=[]
    import csv
    pfile  = open('Password.dat', "r+")
    sread= csv.reader(pfile)
    for row in sread:
        passw+=row
    passw=passw[0]
    return passw
