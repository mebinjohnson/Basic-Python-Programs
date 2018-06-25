import csv
from Functions import *
#___________________________________________________________________________________________________________________________________________________
head=("\eModify Student Record")
design1='*'*75
design2='*'*25
design3='_'*80

print design2.center(80)
print head.center(80)
print design2.center(80)
#___________________________________________________________________________________________________________________________________________________

adno=raw_input("Enter the Admssion Number of Student : ")

print

list=open_student()

pos=-1
for x in range (len(list)):
   if str(list[x][0])==str(adno):
            print "\tMatch Found with Student-",list[x][1]
            pos=x
            break

print design3.center(80)


while pos!=-1:
    print " Select Options Below to Modify Record :- "
    opt=['Change Name', 'Change Class', 'Change Section','Change House']
    for x in range (len(opt)):
        print '\t',x+1,'. ',opt[x]

    selct=raw_input("\nEnter Your Selection : ")

    print design3.center(80)
    if selct=='1':
       new_name=raw_input("Enter Name Modification : ")
       list[pos][1]=new_name
       print  new_name
    elif selct=='2':
        list[pos][4]=raw_input("Enter New Class : ")
        
    elif selct=='3':
        new_section=raw_input("Enter New Class : ")
        list[pos][5]=new_section
    elif selct=='4':
         new_house=raw_input("Enter New House: ")
         list[pos][6]=new_house
    else:
         break
    print "\n\tModification Successfull"
    print design3.center(80)
    print "New Modified Record :-\n"
    print '\tAdmin Number\t\t :',list[pos][0]
    print '\tName of Student\t\t :',list[pos][1]
    print '\tGrade\t\t\t :',list[pos][4]
    print '\tSection\t\t\t :',list[pos][5]
    print '\tHouse\t\t\t :',list[pos][6]
    break
else:
    print design3.center(80)
    print "Match Not Found with Admin Number"


student_save(list)

#___________________________________________________________________________________________________________________________________________________
menu_end()
