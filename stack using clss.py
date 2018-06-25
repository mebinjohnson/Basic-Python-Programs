class stack:
    s=[]
    def push(self):
        lst=[]
        no=int(input("enter any number:"))
        nm=raw_input("enter any name:")
        lst=[no,nm]
        stack.s.append(lst)
        

    def pop(self):
         
        if  stack.s==[]:
            return underflow
        else:
             print stack.s.pop()

    def display(self):
        for i in range(len(stack.s)-1,-1,-1):
            print stack.s[i]

##########   main
item=stack()  # to create an object


c='y'
               
while (c=='y'):
    print'1.PUSH'
    print '2.POP'
    print '3.Display'
    print '4. Exit'
    
    ch=int(input('Enter your choice :'))

    if ch==1:
        item.push()
        
    elif ch==2:
        if item.s==[]:
            print 'empty'
        else:
            item.pop()           

    elif ch==3:
        item.display()
   
    elif ch==4:
         break
    else:
        print 'invalid choice'
        
    c=raw_input('Do you want to continue(y/n) :')
        
