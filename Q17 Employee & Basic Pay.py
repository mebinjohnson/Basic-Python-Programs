class employee(object):
    def __init__(self,no,name,desig,addr,phone,):
        self.emp_no=no
        self.emp_name=name
        self.emp_designation=desig
        self.emp_address=addr
        self.emp_phone=phone

    def getdata(self):
        self.emp_no=int(input('Enter Emplyee Number: '))
        self.emp_name=raw_input("Enter Name of Employee: ")
        self.emp_designation=raw_input("Enter Designation of Employee: ")
        self.emp_address=raw_input("Enter Employee Adress: ")
        self.emp_phone=int(input('Enter Emplyee Phone Number: '))

    def putdata(self):
        print self.emp_no,  self.emp_name, self.emp_designation,self.emp_address,self.emp_phone

class salary(employee):
    def __init__(self,basic,da,hra,gross,pf,tax,net):
        self.basic=basic
        self.da=da
        self.hra=hra
        self.gross=gross
        self.pf=pf
        self.incometax=tax
        self.net=net

    def getdata1(self):
        employee.getdata(self)
        self.basic=int(input("Enter Basic of Employee: "))

    def calc(self):
        
