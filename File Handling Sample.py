import pickle
import os
class flight:
             def __init__(self, fno=101,name="Jet Airways",cap=100.0): 
                          self.fno=fno
                          self.name=name
                          self.cap=cap                                 

             def disp(s):
                          print "\nFlight Number :  " , s.fno
                          print "Name :  " , s.name
                          print "Capacity :  " , s.cap                                                

             def input(s):
                        try:   
                          s.fno=int(raw_input("Enter the flight no :" ))
                          s.name=raw_input("Enter the name :" )
                          s.cap=int(raw_input("Enter the capacity :" ))
                        except ValueError:
                             print("Invalid Input")
                             
             def __str__(s):
                 return "flight no :" + str(s.fno )   + "   name : "  + s.name +"   marks  : "   +  str(s.cap) 

#################################################
#Add record on file
def add():
    file1=open("flight.log",'ab+')
    obj=flight()
    obj.input()   
    pickle.dump(obj,file1)
    file1.close()

#reading from file 
def read():
    file1=open("flight.log",'rb+')
    file1.seek(0)
    try:
             while True:
                               print file1.tell( )       
                               obj=pickle.load(file1)                             
                               obj.disp()
    except EOFError:
                          file1.close()  

    file1.close()
###################
def deleterec():
    file1=open("flight.log",'rb+')
    temp=open("studtemp.log",'ab+')
    fno=input('enter the flight number to be delete :')
    found=False
    try:
                 while True:
                               obj=pickle.load(file1)
                               if obj.fno==fno:
                                    found=True
                               else  :  
                                   pickle.dump(obj,temp)
    except EOFError:
                          file1.close()  
    file1.close()
    temp.close()
    if found==False:
            print('Flight number does not exist')
    else :       
      os.remove("flight.log")
      os.rename("studtemp.log","flight.log")

#############
def main():
    menu='''
        ******Flight Menu*****
          1.to addentry
          2.to display
          3.to delete
          4.to exit
        *******************'''

    while True:
        try:
            print menu
            choice=int(raw_input('Enter the choice(1-4)'))
            if choice==1:
                add()
            elif choice==2:
                  read()  
            elif choice==3:
                deleterec()
            elif choice==4:
                break
            else:
                print('invalid choice')
        except ValueError:
            print('invalid choice')

##############
if __name__=="__main__":
    main()
        
            
        
