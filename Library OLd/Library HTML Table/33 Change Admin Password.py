from Functions import *
#___________________________________________________________________________________________________________________________________________________
design('*',25)
design('Change Admin Password',1,)
design('*',25)
#___________________________________________________________________________________________________________________________________________________
bfile  = open('password.txt', "rb")
passw='trial'
for row in bfile:
        passw=row

#print passw

old=raw_input("Enter Current Admin Password: ")
design('_',80)
if (old or 'trial')  in passw:
   new_password=raw_input("\nEnter New Password:")
   re_enter=raw_input("\nRe-enter New Password:")
   if new_password!=re_enter:
      print "\n\tNew Password Do not Match"
   else:
        ofile  = open('password.txt', "w")
        ofile.write(new_password)
        design('_',80)
        print "\n\tPassword Succesfully Updated"
else:
    print "\n\tWrong Password"
#___________________________________________________________________________________________________________________________________________________
menu_end()

