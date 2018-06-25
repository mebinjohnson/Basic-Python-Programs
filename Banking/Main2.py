import os
import datetime
import pickle

#_________________________________________________________________________________________________
class customer:
    def __init__(self,cid=0):
        self.id=cid
        self.name=''
        self.address=''
        self.mobile=''
    def store(self):
        self.name=raw_input('Enter your name : ')
        self.address=raw_input('Enter your address : ')
        self.mobile=raw_input('Enter your mobile number : ')
    def display(self):
        print 'Customer ID: \t',self.id
        print 'Customer Name: \t',self.name
        print 'Customer Address: \t',self.address
        print 'Customer Mobile: \t',self.mobile
        print

class transaction:
    def __init__(self):
        self.cus_id=0
        self.amnt=0
    def store(self):
        self.amnt=input('Enter the amount to be deposited : ')
    def display(self):
        print 
        print 'Amount In Your Account : ',self.amnt,' AED'
        today=datetime.date.today()
        print 'Date: ',today
        print
#_________________________________________________________________________________________________
def create(cid):
    try:
        f1=open("customer.dat","rb")
    except (IOError,OSError) :
        print "Creating New Data !"
        f1=open("customer.dat",'wb+')
    
    read_data=[]
    try:
        while True:
            obj=pickle.load(f1)
            read_data.append(obj)           
    except EOFError:
        f1.close()
    status=0
    f3=open("customer.dat","ab")
    for x in read_data:
        if x.id==cid:
            status=1
            break
    if status!=1:
        print'\n\tCreating a New Account .....\n'
        b=customer(cid)
        b.store()
        s=b.id
        pickle.dump(b,f3)
        f1.close()

        f2=open("transaction.dat","ab")
        t=transaction()
        t.cus_id=s
        t.store()
        pickle.dump(t,f2)
        f2.close()
    else:
        print "\tCustome ID Already in Use"
#_________________________________________________________________________________________________

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
        print '\tCustomer Not Found'
#_________________________________________________________________________________________________

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
    if status!=1:
        print "\tTransaction Data Not Found"

                
#_________________________________________________________________________________________________
    
def deposit(id):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                a=input('Enter The Amount To Be Deposited')
                t.amnt=t.amnt+a
                status=1
            pickle.dump(t,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print '\tAmount Deposited'
    else:print'\tCustomer Not Found'
#_________________________________________________________________________________________________

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
                    a=input('Enter The Amount To Be Withdrawn:')
                    if a<t.amnt:
                        t.amnt=t.amnt-a
                        status=1
                    else:
                        
                        status=2
            pickle.dump(t,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print '\tProcess Complete'
    elif status==2:
        print '\tAccount Balance is not Sufficient.' 

    else:
        print'\tCustomer Not Found'
#_________________________________________________________________________________________________

'''
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
    else:
        print'Customer Not Found'
#_________________________________________________________________________________________________


def transfer(id):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                a=input('Enter The Amount To BE Transfered')
                if a<=t.amnt:
                    
                    #t.amnt=t.amnt-a
                    status=1
                else:
                    status=2
            
    except EOFError:
        f1.close()
        f2.close()
    
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Process Complete'
    elif status==2:
        print 'Insufficient Balance. '
    else:print'Customer Not Found'
    id2=input('Enter The Reciever Account ID: ' )
    #customertransfer(id2,a)

    k1=open("transaction.dat","rb")
    k2=open("newfile.dat","ab")
    status=0
    r=transaction()
    try:
        while True:
            r=pickle.load(k1)
            if r.cus_id==id:
                r.amnt=r.amnt+amnt
                status=1
            pickle.dump(r,k2)
            pickle.dump(t,k2)
    except EOFError:
        k1.close()
        k2.close()
        
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Amount Transfered'
    else:
        print'Customer Not Found'

#_________________________________________________________________________________________________

def transferamnt(id):
    f1=open("transaction.dat","rb")
    f2=open("newfile.dat","ab")
    status=0
    t=transaction()
    try:
        while True:
            t=pickle.load(f1)
            if t.cus_id==id:
                a=input('Enter The Amount To BE Transfered')
                if a<=t.amnt:
                    id2=input('Enter The Reciever Account ID: ' )
                    try:
                        while True:
                            r=pickle.load(f1)
                            if r.cus_id==id2:
                                r.amnt=r.amnt+a
                                t.amnt=t.amnt-a
                                status=1
                                pickle.dump(r,f2)
                                pickle.dump(t,f2)
                            else:
                                status=2
                    
                    except EOFError:
                        #f1.close()
                        #f2.close()
                        pass
                else:
                    status=3
            else:
                status=4
    except EOFError:
        #pass
        f1.close()
        f2.close()
       
    os.remove("transaction.dat")
    os.rename("newfile.dat","transaction.dat")
    if status==1:
        print 'Amount Transfered'
    elif status==2:
        print "Recievers Account is Not Found"
    elif status==3:
        print "Amount Not Sufficient."
    elif status==4:
        print'Customer Not Found !'
'''
#_________________________________________________________________________________________________

def transferamnt(id):
    #customer_data=opencust()
    status=1
    trans_data=opentrans()
    f=open('transaction.dat','wb')
    for customer in trans_data:
        if customer.cus_id==id:
            a=input('Enter The Amount To BE Transfered: ')
            if a<=customer.amnt:
                id2=input('Enter The Reciever Account ID: ' )
                for reciever in trans_data:
                    if reciever.cus_id==id2:
                        customer.amnt=customer.amnt-a
                        print "Current Available Balance : ",customer.amnt
                        reciever.amnt=reciever.amnt+a
                        print
                        print "\tAmount Transfered"
                        status=0           
            else:
                print "\tAmount Insufficient"
    for data in trans_data:
                            pickle.dump(data,f)
    if status==1:
        print "\tReceiver Account Not Found"
    f.close()
    
        
#_________________________________________________________________________________________________
      

def opencust():
    f=open("customer.dat","rb")
    c=customer()
    list=[]
    try:
        while True:
            c=pickle.load(f)
            list.append(c)
    except EOFError:
        f.close()
    return list

#_____________________________________________________________________

def opentrans():
    f=open("transaction.dat","rb")
    c=transaction()
    list=[]
    try:
        while True:
            c=pickle.load(f)
            list.append(c)
    except EOFError:
        f.close()
    return list

    

#_________________________________________________________________________________________________
def displayall():
    data=opencust()
    print
    print '-'*150
    print '|','ID\t','|','Customer Name\t','|','Address\t\t\t','|','Mobile','|'
    print '-'*150
    for customer in data:
        
        print '|',customer.id,'\t|',customer.name,'\t|',customer.address,'      |',customer.mobile,"\t|"
#_________________________________________________________________________________________________
    
def main():
        while True:
            print '~'*80
            print ('*'*10).center(80)
            print 'CBI Bank'.center(80)
            print ('*'*10).center(80)
            print '~'*80
            functions=['New Customer','Display Customer','Deposit amount','Withdraw Amount','Transfer Amount','Display All Customers','Exit Application']
            cnt=1
            for x in functions:
                print '\t|',cnt,'-\t',x
                cnt+=1
#
            ch=raw_input('\nEnter your Choice : ')
            print
            print "~"*80
            if ch=='1':
                id=input('Enter The Customer ID : ')
                create(id)
        
            elif ch=='2':
                id=input('Enter The Customer ID : ')
                display(id)
                displaytran(id)
            
            elif ch=='3':
                id=input('Enter The Customer ID : ')
                display(id)
                deposit(id)
            elif ch=='4':
                id=input('Enter The Customer ID : ')
                display(id)
                withdraw(id)
            elif ch=='5':
                id=input('Enter The Customer ID : ')
                #transfer(id)
                transferamnt(id)
            elif ch=='6':
                displayall()
            elif ch=='7':
                exit()
            else:
                print'\n\tWrong choice Entered'
            raw_input()
            import subprocess as sp
            sp.call('cls',shell=True)
        
main()          
