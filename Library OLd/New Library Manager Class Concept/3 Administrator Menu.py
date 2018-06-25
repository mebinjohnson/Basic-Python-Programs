from Functions import *
design('*',25)
design('Administrative Menu',1)
design('*',25)
design('_',80)

#____________________________________________________________________________________________________________________________________________________
print
menu=[' Display All Student Record',' Modify Student Record',' Change Admin Password',' Create Book',' Display All Books',' Delete Book',' View Book',' View Student Record',' View Issued Books','Back to Main Menu']
for x in range (len(menu)):
    print '\t',x+1,'. ',menu[x]


design('_',80)
select=raw_input("Enter Your Selection (1-10): ")

import subprocess as sp
sp.call('cls',shell=True)



if select=='1':
    execfile( "31 Student Record.py")
if select=='2':
    execfile( "32 Modify Student Record.py")
elif select=='5':
    execfile( "35 Books Record.py")
elif select=='10':
    execfile( "0 Main.py")
elif select=='7':
    execfile( "37 View Book.py")
elif select=='8':
    execfile("38 View Student.py")
elif select=='9':
    execfile("39 View Issued Books.py")
elif select=='6':
    execfile("36 Delete Book.py")
elif select=='4':
    execfile("34 Create Book.py")
elif select=='3':
    execfile('33 Change Admin Password.py')
else:
    execfile('3 Administrator Menu.py')
    


raw_input ()
