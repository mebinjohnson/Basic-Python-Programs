from Functions import *
#___________________________________________________________________________________________________________________________________________________
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
#___________________________________________________________________________________________________________________________________________________
