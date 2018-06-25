def design(char,no):
    design=str(char)*int(no)
    print design.center(80)
#___________________________________________________________________________________________________________________________________________________
def refresh(file):
    execfile( str(file))    
#___________________________________________________________________________________________________________________________________________________  

def menu_end():
    design3='_'*80
    print design3.center(80)
    print ("Selection:\n\t1. Main Menu \n\t2. Administrator Menu \n\t3. Exit")
    select=raw_input("Enter Selection (1-3) : ")

    import subprocess as sp
    sp.call('cls',shell=True)

    import os
    if select=='3':
        exit()
    if select=='2':
        execfile( "3 Administrator Menu.py")
    else:
        execfile( "0 Main.py")
#___________________________________________________________________________________________________________________________________________________

def open_book():
    import csv
    bfile  = open('Books.csv', "rb")
    books = csv.reader(bfile)
    list2=[]
    for row in books:
        list2+=[row]
    return list2
#___________________________________________________________________________________________________________________________________________________
def open_student():
    import csv
    bfile  = open('Student ID.csv', "rb")
    books = csv.reader(bfile)
    list=[]
    for row in books:
        list+=[row]
    return list
#___________________________________________________________________________________________________________________________________________________
def list_search(num,list):
    for x in range (len(list)):
       if str(list[x][0])==str(adno):
           pos=x
           break
    return pos
#___________________________________________________________________________________________________________________________________________________    
def book_save(list):
    import csv
    bofile  = open('Books.csv', "wb")
    bwriter = csv.writer(bofile)
    for row in list:
        bwriter.writerow(row)
#___________________________________________________________________________________________________________________________________________________
def student_save(list):
    import csv
    ofile  = open('Student ID.csv', "wb")
    writer = csv.writer(ofile)
    for row in list:
        writer.writerow(row)
#___________________________________________________________________________________________________________________________________________________
def password():
    bfile  = open('password.txt', "rb")
    for row in bfile:
        return row
#___________________________________________________________________________________________________________________________________________________



