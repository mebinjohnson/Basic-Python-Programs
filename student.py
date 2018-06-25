student={}# empty dictionary

def addEntry():
    name=raw_input('enter the name ')
    rollno=int(raw_input('enter the rollno '))
    age=int(raw_input('enter the age '))
    Class=raw_input('enter the class ')
    student[rollno]=[name,age,Class]

def removeEntry():
    rollno=int(raw_input('enter the roll no to be deleted '))
    print('the value deleted is',student.pop(rollno,'does not exist'))

def modify():
    rollno=int(raw_input('enter the rollno of the person to update '))

    L=student.pop(rollno)

    print('the existing name is',L[0])

    ans=raw_input('do you have to update this(Y/N)')
    
    if ans.upper()=='Y':
              L[0]=raw_input('enter the new name')

    student[ rollno]=L
    
def allEntry():
      print student

def menu():
             
             menu="""
                 ******Student menu******
                    1.Add                
                    2.Remove
                    3.Modify
                    4.Display All
                    5.Quit
                
                ***********************"""
             while True:
                  try:
                      print(menu)
                      choice=int(raw_input('enter the choice(1-5)'))
                      if choice==1:
                          addEntry()
                      elif choice==2:
                          removeEntry()
                      elif choice==3:
                          modify()
                      elif choice==4:
                          allEntry()
                      elif choice==5:
                           break
                      else:
                          print('invalid choice')

                  except ValueError:
                          print('inappropriate value')
                          
if __name__=='__main__':
              menu()
              
              
              
                          
                          
                          
                              
              
              
              
                    
