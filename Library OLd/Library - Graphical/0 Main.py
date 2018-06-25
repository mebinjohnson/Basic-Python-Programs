from Functions import *
from Tkinter import *
from ttk import *

def bookissue():
    execfile( "1 Book Issue.py")
def bookdeposit():
    execfile( "2 Book Deposit.py")
def adminmenu():
    execfile( "3 Administrator Menu.py")

#___________________________________________________________________________________________________________________________________________________

root=Tk()

root.title("Library Manager")
root.geometry("300x350")
'''
style = Style()
style.configure("TFrame", background="#333")
'''
app=Frame(root,)
app.grid()
head1=Label(app,text="GEMS OUR OWN INDIAN SCHOOL, DUBAI",font=("Helvetica", 8))
head1.grid()

Book_Issue=Button(app,compound=LEFT,text="Book Issue" ,command=bookissue)
Book_Issue.grid()

Book_Deposit=Button(app,text="Book Deposit" ,command=bookdeposit)
Book_Deposit.grid()

Admin_Menu=Button(app,text="Administrator Menu" ,command=adminmenu)
Admin_Menu.grid()

root.mainloop()


#___________________________________________________________________________________________________________________________________________________




'''
design('*',75)
design("GEMS OUR OWN INDIAN SCHOOL, DUBAI",1)
design('*',75)
design("Main Menu",1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________

print ("\t1. Book Issue \n\t2. Book Deposit\n\t3. Administrator Menu\n\t4. Exit")
print
select=raw_input("Enter Your Selection (1-4): ")

import subprocess as sp
sp.call('cls',shell=True)
#___________________________________________________________________________________________________________________________________________________
if select=='1':
    execfile( "1 Book Issue.py")
if select=='2':
    execfile( "2 Book Deposit.py")
elif select=='3':
    execfile( "3 Administrator Menu.py")
elif select=='4':
    exit()
else:
    execfile( "0 Main.py")
'''
#___________________________________________________________________________________________________________________________________________________
