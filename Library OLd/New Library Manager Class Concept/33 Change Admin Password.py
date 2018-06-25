from Functions import *
#___________________________________________________________________________________________________________________________________________________
design('*',25)
design('Change Admin Password',1,)
design('*',25)
#___________________________________________________________________________________________________________________________________________________
pfile  = open('Password.dat', "r+")
passw=[]

import csv
pfile  = open('Password.dat', "r+")
sread= csv.reader(pfile)
for row in sread:
        passw+=row

print passw
old=raw_input("Enter Current Admin Password: ")
design('_',80)

if [str(old)]==passw:
   new_password=raw_input("\nEnter New Password:")
   re_enter=raw_input("\nRe-enter New Password:")
   if new_password!=re_enter:
      print "\n\tNew Password Do not Match"
   else:
        print new_password
        pfile.write(new_password)
        design('_',80)
        print "\n\tPassword Succesfully Updated"
else:
    print "\n\tWrong Password"
if passw==[]:
        print '\n\tPassword Hacked'
pfile.close()
#___________________________________________________________________________________________________________________________________________________
menu_end()

