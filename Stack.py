class employee:
    emp_stack=[]
    def __init__(self,empno=00,name='',sal=0):
        self.empno=empno
        self.name=name
        self.salary=sal
    def add(self):
        self.empno=int(input('Enter Employee Number: '))
        self.name=raw_input("Enter Employee Name: ")
        self.salary=int(input("Enter Salary: "))

    def __str__(self):
        return str(self.empno)+'  '+self.name+'     '+str(self.salary)

data_list=[]

def pop(dlist):
    if dlist!=[]:
        x=dlist.pop()
        return x
    else:
        return 'Is Empty'
def push(dlist):
    obj=employee()
    obj.add()
    dlist.append(obj)
def view(dlist):
    for obj in dlist:
        print obj
c='y'
data_list=[]  
while (c=='y'):
    print'1.PUSH'
    print '2.POP'
    print '3.Display'
    print '4. Exit'
    
    ch=int(input('Enter your choice :'))

    if ch==1:
        push(data_list)
        
    elif ch==2:
        if item.s==[]:
            print 'empty'
        else:
            pop(data_list) 

    elif ch==3:
        pass
   
    elif ch==4:
         break
    else:
        print 'invalid choice'
        
    c=raw_input('Do you want to continue(y/n) :')
        

