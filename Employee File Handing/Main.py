import pickle
class emp:
    def __init_(self,empno=0,empname='',salary=0):
        self.empno=empno
        self.empname=empname
        self.salary=salary
    def add(self):
        self.empno=int(input("Enter Employee Number: "))
        self.empname=raw_input("Enter name of Employee: ")
        self.salary=int(input("Enter Salary of Employee: "))
def open_file():
    data_list=[]
    f=open("Data.log","rb+")
    try:
        while True:
            data_list+=[pickle.load(f)]
    except EOFError:
        f.close()
    print '\t >>Opening File'
    print data_list
    return data_list
    
def save_file(list):
    f=open("Data.log","wb+")
    print '\t >>Writing on File'
    for objects in list:
        pickle.dump(objects,f)
    
    f.close()

def main():
    print '*'*80
    print "Danway Group of Companies".center(80)
    print '*'*80
    cnt=1
    
    func=['Add','Search by Name','Display All','Exit']
    for f in func:
        print '\t',cnt,'.  ',f
        cnt+=1
    print '_'*80
    select=raw_input('Enter  your selection: ')
    print
    print '_'*80

    if select=='1':
        obj=emp()
        obj.add()
        data_list=open_file()
        data_list.append(obj)
        print data_list
        save_file(data_list)
    

    elif select=='2':
        name=raw_input("Enter Name of Employee to Search: ")
        data_list=open_file()
        for x in data_list:
            if x.empname==name:
                print 'Employe Number :\t',x.empno
                print 'Employe Name :\t',x.empname
                print 'Employe Salary :\t',x.salary
                break
    elif select=='3':
        data_list=open_file()
        print 'Employee No\t|\tEmployee Name\t|\tSalary'.center(80)
        for x in data_list:
            print (str(x.empno)+'\t|\t'+str(x.empname)+'\t|\t'+str(x.salary)).center(80)
main()
        
    
    
    
        
        


        
        
