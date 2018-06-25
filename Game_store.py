import pickle
import time
#_______________________________________________________________________________________
import platform
import os
def clear():
    operSys = platform.system()
    if operSys.lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')
#_______________________________________________________________________________________
class games():
    def __init_(self,number,name,price,quantity):
        self.number=number
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def add(self):
        try:
            data_list=open_data()
            self.number=int(raw_input('Enter serial number:\t'))
            status=0
            for x in data_list:
                if x.number==self.number:
                    status=1
                    break
            if status==1:
                print "Serial Number Already in Use"
            else:
                self.name=(raw_input("Input Game Title:\t")).upper()
                self.price=float(raw_input('Input Price of Game:\t'))
                self.quantity=int(raw_input('Input Number of Items:\t'))
        except ValueError:
            print "Error ......input only numbers"
            
#_______________________________________________________________________________________
def add_data():
    obj=games()
    obj.add()
    f=open('data.log','ab+')
    pickle.dump(obj,f)
    f.close
#_______________________________________________________________________________________
def open_data():
    f=open('data.log','ab+')
    data_list=[]
    try:
        while True:
            x=pickle.load(f)
            data_list.append(x)
    except EOFError:
        f.close
    return data_list
#_______________________________________________________________________________________
def view_all():
    data_list=open_data()
    print '_'*80
    print '|S No.\t|\tName\t\t|\tQuantity|'
    print '_'*80
    for x in data_list:
        print '|', x.number,'\t|\t', x.name,'\t\t|\t', x.quantity,''
    print '_'*80
#_______________________________________________________________________________________

def search(sname):
    data_list=open_data()
    s=0
    for game in data_list:
        if game.name==sname:
            print "Title of Game: ",game.name,
            print '\nPrice of the Game:\t',game.price,
            print '\nQuantity of games:\t ',game.quantity
            s=1
            break
    if s==0:
        print "NOT FOUND"
#_______________________________________________________________________________________
def modify(no):
    data_list=open_data()
    print
    s=1
    for x in data_list:
        if x.number==no:
            search(x.name)
            print "1. Change Name"
            print "2. Change Price"
            print "3. Change Quantity"
            s=0
            
            select=int(raw_input("Enter Choice: \t"))
            if select==1:
                x.name=(raw_input("Enter Title:\t ")).upper()
            elif select==2:
                x.price=float(raw_input('Enter Price:\t'))
            elif select==3:
                x.quantity=int(raw_input('Enter Quantity:\t'))
            else:
                print "Wrong Choice"
                
            break
    if s==1:
        print "NOT FOUND"
            

    f=open('data.log','wb+')
    for obj in data_list:
        pickle.dump(obj,f)
    f.close
#_______________________________________________________________________________________        

def purchase():
    data_list=open_data()
    view_all()
    trolley=[]
    p=''
    #no=int(raw_input("Enter Serial: "))
    print
    while True:
        no=int(raw_input("Enter Serial:\t "))
        s=0
        for x in data_list:
            if x.number==no:
                    s=1
                    quantity=int(raw_input("Enter Quantity:\t"))
                    if quantity<=x.quantity:
                        item=[x.name,quantity,x.price,(x.price*quantity)]
                        x.quantity-=quantity
                        trolley.append(item)
                        
                        print
                                          
                    else:
                        print 'Quantity Not Enough'
        if s==0:
            print "SERIAL NOT FOUND"
        p=raw_input("yes/no continue")
                    
        if p!='yes':
                            break                
            
        
            
    print "Reciept"
    total=0
    print '_'*50
    print 'Title\tQuantity\tPrice\tTotal Price'
    print '_'*50
    for x in trolley:
        
        print x[0],'\t',x[1],'\t',x[2],'\t',x[3]
        print '-'*50
        total+=x[3]
    print '_'*50
    print "Total: ",total
    print '_'*50

    f=open('data.log','wb+')
    for obj in data_list:
        pickle.dump(obj,f)
    f.close

    
#_______________________________________________________________________________________
def main():
    features=['Add','View All','Modify','Search by Title','Purchase','Exit']
    print '*'*80
    print '\t\tRevivo Games Enterprises'
    print '*'*80
    cnt=1
    for f in features:
        print '\t',cnt,f
        cnt+=1
    print
    try:
        selection=raw_input("Enter Your Selection: \t")
        if selection=='1':
            add_data()
        elif selection=='2':
            view_all()
        elif selection=='4':
            sname=(raw_input("Enter Title to Search:\t ")).upper()
            search(sname)
        elif selection=='3':
            no=int(raw_input('Enter serial number:\t'))
            modify(no)
        elif selection=='5':
            purchase()
        elif selection=='6':
            print 'Thank you for using Revivo Game Store. The application will close shortly..........'
            n=5
            while n > -1:
                        time.sleep(1)
                        print '\t\t\t'+ str(n)
                        n = n-1
            exit()
        else:
            print "Wrong Choice"
        raw_input()
        clear()
    except ValueError:
        print "Error enter number"
while True:
    main()
