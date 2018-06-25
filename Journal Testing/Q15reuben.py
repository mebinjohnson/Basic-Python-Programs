Student = list() # A default stack using list() function.
top = -1 # To know the current index position in Stack.

#Adding element into a stack.
def PUSH(Student, top): 
   Ch = 'Y' 
   while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
      Rollno = int(input("Enter roll number: "))
      Name = raw_input("Enter name: ") 
      std = (Rollno, Name) # Creating a tuple
      Student.append(std) # A tuple added into a list
      top += 1 # It check the total number of addition
      print ("Do you want to add more...<y/n>: ")
      Ch = raw_input() 
      if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
         break 
   return top 

#Removing stack elements 
def POP(Student, top):
   slen = len(Student)   # Finds total elements in the stack.
   if slen <= 0:   # Checks if stack is either empty or not.
      print ("Stack is empty")
   else:
      Rollno, Name = Student.pop() # Removing top elements from Student stack.
      top = top - 1

      print("Value deleted from stack is", Rollno, Name)
   return top

# Showing stack elements
def SHOW(Student, top):
   slen = len(Student) # Finds total elements in the Student stack.
   if slen <= 0: # Checks if stack is either empty or not.
      print ("Stack is empty")
   else:
      print("The stack elements are...")
      i = top
      while (i >= 0): # Student stack processed in reverse order.
         Rollno, Name = Student[i]
         print(Rollno, Name)
         i -= 1

while (True):
   print()		
   print('S T A C K	O P E R A T I O N')
   print('- - - - - - - - - - -	- - - - -')
   print('1. Add Student Data')	
   print('2. Remove Student Data')
   print('3. Display Student Data')
   print('4. Stop operation')

   Opt = input( "Enter your option: ")
   print()
   if (Opt == 1) :

      # Push operation of stack
      top = PUSH(Student, top)
      
   elif (Opt == 2) :

      # Pop operation of stack
      top = POP(Student, top)
   elif (Opt == 3) :
      SHOW(Student, top)

   elif (Opt == 4) :
      break

