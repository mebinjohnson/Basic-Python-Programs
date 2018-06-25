import os
import datetime
import pickle

class customer:
    def __init__(self):
        self.id=0
        self.name=''
        self.address=''
        self.mobile=''
    def store(self):
        self.id=input('\nEnter customer id - ')
        self.name=raw_input('Enter your name - ')
        self.address=raw_input('Enter your address - ')
        self.mobile=raw_input('Enter your mobile number - ')
    def display(self):
        print self.id
        print self.name
        print self.address
        print self.mobile

class transaction:
    def __init__(self):
        self.cus_id=0
        self.amnt=0
    def store(self):
        self.amnt=input('Enter the amount to be deposited')
    def display(self):
        print 'Amount In Your Account',self.amnt
        today=datetime.date.today()
        print today

def create():
    print'\nCreating a new account.....\n'
    f1=open("customer.dat","ab")
    b=customer()
    b.store()
    s=b.id
    pickle.dump(b,f1)
    f1.close()

    f2=open("transaction.dat","ab")
    t=transaction()
    t.cus_id=s
    t.store()
    pickle.dump(t,f2)
    f2.close()
def display(id):
    f=open("customer.dat","rb")
    c=customer()
    status=0

    try:
        while True:
            c=pickle.load(f)
            if c.id==id:
                status=1
                c.display()
    except EOFError:
        f.close()
    if status==0:
        print 'customer Not Found'
def displaytran(id):        
    f1=open("transaction.dat","rb")
    t=transaction()
    status=0

    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                status=1
                t.display()
    except EOFError:
        f1.close()
    if status==0:
        print 'customer Not Found'
                
    
def deposit(id):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                a=input('Enter The Amount To Be deposited')
                t.amnt=t.amnt+a
                status=1
            pickle.dump(t,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Amount Deposited'
    else:print'Customer Not Found'

def withdraw(id):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                if t.amnt>0:
                    a=input('Enter The Amount To BE withdrawn')
                    t.amnt=t.amnt-a
                    status=1
                else:print 'Account Balance is 0'
            pickle.dump(t,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Process Complete'
    else:print'Customer Not Found'

def customertransfer(id,amnt):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                t.amnt=t.amnt+amnt
                status=1
            pickle.dump(t,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Amount Transfered'
    else:print'Customer Not Found'


def transfer(id):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                if t.amnt>0:
                    a=input('Enter The Amount To BE Transfered')
                    t.amnt=t.amnt-a
                    status=1
                else:print 'Account Balance is 0'
                status=1
            pickle.dump(t,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Process Complete'
    else:print'Customer Not Found'
    id2=input('Enter The Account ID To whom the money has to be transfered:')
    customertransfer(id2,a)
    

              
    
def main():
        while True:
            print'\n\n1-New Customer\n2-DisplayCustomer\n3-Deposit amount\n4-Withdraw Amount\n5-Transfer\n6-Exit'

            ch=input('\nEnter your choice - ')

            if ch==1:
                create()
        
            elif ch==2:
                id=input('Enter The customer ID')
                display(id)
                displaytran(id)
            
            elif ch==3:
                id=input('Enter The customer ID')
                display(id)
                deposit(id)
            elif ch==4:
                id=input('Enter The customer ID')
                display(id)
                withdraw(id)
            elif ch==5:
                id=input('Enter The customer ID')
                transfer(id)
            elif ch==6:
                exit()
            else:
                print'\nWrong choice entered'
        
main()          
              

                
                
    
    
