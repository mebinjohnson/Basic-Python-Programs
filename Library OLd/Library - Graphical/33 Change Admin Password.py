from Functions import *

design('*',25)
design('Change Admin Password',1,)
design('*',25)


bfile  = open('password.txt', "rb")
for row in bfile:
        passw=row
old=raw_input("Enter Previous Admin Password: ")
if old==passw:
   new_password=raw_input("\nEnter New Password:")
   re_enter=raw_input("\nRe-enter New Password:")
   if new_password!=re_enter:
      print "\n\tNew Password Do not Match"
   else:
        
        ofile  = open('password.txt', "w")
        ofile.write(new_password)
        print "\n\tPassword Succesfully Updated"
else:
    print "\n\tWrong Password"

menu_end()

