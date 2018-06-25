# Person base class or super class 

class Person(object):
    def __init__(self, name, age, psex):
        self.pname = name
        self.page = age 
        self.psex = psex

    def Person_inputData(self):
        self.pname = raw_input("Enter name: ") 
        self.page = input("Enter age: ") 
        self.psex = raw_input("Enter gender: ")
        print


    def Person_Display(self): 
        print ("Person's information....")
        print ("==========================") 
        print ("Teacher detail is:")
        print ("==========================") 
        print "Name: ", self.pname
        print "Age: ", self.page 
        print "Sex: ", self.psex

# Employee base class or super 

class  Employee(object): 

    def __init__(self, ecode, edesig,  esalary):
        self.empcode = ecode 
        self.empdesig = edesig 
        self.empsalary = esalary 

    def Emp_inputData(self):
        self.empcode = raw_input("Enter code: ") 
        self.empdesig = raw_input("Enter designation: ") 
        self.empsalary = raw_input("Enter basic salary: ") 

    def Emp_Display(self):
        print "Code: ", self.empcode 
        print "Designation: ", self.empdesig
        print "Salary: ", self.empsalary 

# Derived class for multiple inheritance 

class Teacher(Person, Employee):
    def __init__(self, a, b, c, d, e, f):
         Person.__init__(self, a, b, c) 
         Employee.__init__(self, d, e, f)
    def get_data(self):
        Person.Person_inputData(self)
        Employee.Emp_inputData(self) 
        # Invoking base class constructors 
        # Invoking base class methods 
    def show_data(self):
        # Invoking base class methods 
        Person.Person_Display(self) 
        Employee.Emp_Display(self)
    
# Main program

T = Teacher(' ', 0, ' ', ' ', ' ', 0)
T.get_data()
T.show_data()
raw_input()
