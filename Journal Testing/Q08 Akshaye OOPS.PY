# Accessing employee information to calculate gross salary 

class Employee:
#Constructor called when creating an object of class type
              def __init__(self, ecode, ename, edesig, esal): 

                             self.empcode = ecode
                             self.empname = ename
                             self.empdesig = edesig
                             self.empbasic = esal 

#	DA calculation method 
              def Calc_DA(self):

                self.__da = self.empbasic * 0.8 # _da is a private attribute
                return self.__da

              # HRA calculation method
              def __Calc_HRA(self):

                self.__hra = self.empbasic * 0.1 # _hra is a private attribute
                return self.__hra

              def Calc_Gross(self):

              # Accessing attributes and methods in class method 
                            empda=self.Calc_DA() # Calling public method thorough

              #reference
                            emphra = self.__Calc_HRA() # Calling private method thorough reference

                            empgross = self.empbasic + empda + emphra
                            return empgross


              # A class method to display employee nformation
              def Display(self):

                print "Here is the employee information...."
                print "=" * 30

                print"Code:", self.empcode
                print"Name:", self.empname
                print"Designation:", self.empdesig
                print"Basic salary:", self.empbasic
 
                print"Dearness Allowance(DA): %.2f" % self.Calc_DA()
                print"House Rent Allowance(HRA): %.2f" % self.__Calc_HRA()
                print"Gross income: %.2f" % self.Calc_Gross()

# Main program starts 

# Enter employee data

print("Enter employee data")


ecode = raw_input("Enter code: ")
ename = raw_input("Enter name: ")
edesig = raw_input("Enter designation: ")
esal = float(input("Enter basic salary: "))
                

Emp = Employee(ecode, ename, edesig, esal)

# Calling the class method using instance object
Emp.Display()
