# -*- coding: cp1252 -*-
import pickle
'''Write a code to create customer’s list with their number & name and delete any particular customer using his /her number. 
'''

def open_data():
    file0=file('data.txt','rb+')
    try :
        customer_list=pickle.load(file0)
    except EOFError:
        print "Empty Data"
        customer_list={}
    file0.close()
    return customer_list

def save_data(cus):
        file1=file('data.txt','wb+')
        pickle.dump(cus,file1)

def add(cust):
    print
    print '-'*75
    print "A d d      N e w       C o n ta c t "
    name=raw_input('Enter name of Contact: ')
    no=raw_input("Enter Contact Number : ")
    cust[name.upper()]=no
    
def view_all(cust_list):
    print
    print "A l l      C o n t a c t s"
    print 
    print '-'*75
    print 'N a m e \t\t C o n t a c t    N u m b e r'
    print '-'*75
    for name in cust_list:
        print name,'\t-\t',cust_list[name]
    print '-'*75
def search():
    print '-'*75
    print "S e a r c h     B y       N a m e"
    print
    s=1
    customer_list=open_data()
    sname=raw_input("Enter Name to Search:\t" ).upper()
    try:
        customer_list[sname]
        print "\n\tC O N T A C T       F O U N D \n"
        print '-'*30
        print '|\tN A M  E\t:\t',sname,'\t|'
        print '|\tN U M B E R\t:\t',customer_list[sname],'\t|'
        print '-'*30

    except KeyError:
        print '\n\tC O N T A C T        C O U L D         N O T         B E         F O U N D         I N         D A T A ' 
def modify():
    print '-'*75
    print "M o d i f y           C o n t a c t "
    print
    s=1
    customer_list=open_data()
    sname=raw_input("Enter Name to Search and Modify :\t" ).upper()
    try:
        print "Found\n\t",sname,'\t',customer_list[sname]
        customer_list[sname]=raw_input("Enter New Number : ")
        save_data(customer_list)
        print
        print "\t CONTACT MODIFIED"

    except KeyError:
        print '\n\tNAME COULD NOT BE FOUND IN DATA'





    
    
def delete():
    name=raw_input("Enter Name to be deleted : ")
    customer_list=open_data()
    try:
        
        del customer_list[name.upper()]
        print 'Contact Deleted'
        save_data(customer_list)
    except KeyError:
        print 'Name Could Not be Found in Data'
    

def main():
    print '-'*75
    print " C O N T A C T S"
    print '-'*75
    functions=['Add New Contact','Delete Contact','Search Contact','View all Contacts','Modify','Exit']
    for f in range (len(functions)):
        print '\t[',f+1,']\t',functions[f]
    print
    sel=int(input("Enter Selection: "))
    print '_'*75

    if sel==1:
        customer_list=open_data()
        add(customer_list)
        save_data(customer_list)
    elif sel==2:
        delete()
    elif sel==3:
        search()
    elif sel==4:
        customer_list=open_data()
        
        view_all(customer_list)
    elif sel==5:
        modify()
    elif sel==6:
        exit()
    else:
        print "Wrong Selection"
    raw_input()

while True:
    try:
        main()

    except IOError:
        print "Wrong Input"
        raw_input()
