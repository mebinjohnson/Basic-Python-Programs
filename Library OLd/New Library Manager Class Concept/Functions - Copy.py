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
    def __init__(self,no=0000,name='',issue='',bookno=0000,grade='',section='',house=''):
        self.student_no=no
        self.student_name=name
        self.student_issue=issue
        self.student_bookno=bookno
        self.student_grade=grade
        self.student_section=section
        self.student_house=house
        Student.total_students+=1
    def display(self):
        print self.student_no,'-',self.student_name
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

import pickle
student_loc=[]
file1=open("Student_ID.log",'rb')
obj=Student()
try:
    while True:
        obj=pickle.load(file1)
        obj.display()
        student_loc.append(obj)
except EOFError:
    file1.close()
        





'''
list=student_class()
import pickle
file1=open("Student_ID.log",'wb')
cnt=0
for x in list:
    pickle.dump(x,file1)
    print cnt
    cnt+=1
file1.close()
'''
#___________________________________________________________________________________________________________________________________________________
