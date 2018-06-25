x='''
 Create the class SOCIETY with following information:
 society_name
 house_no
 no_of_members
 flat
 income
 Methods An __init__ method  to assign initial values of society_name as "Surya Apartments", flat as "A Type", house_no as 20, no_of_members as 3,
 income as 25000.
 Inputdata( ) - to read data members(society,house_no,no_of_members&income) and call
 '''

class SOCIETY(object):
    def input_data(self):
        self.society_name=raw_input("Enter Society:")
        self.house_no=int(raw_input("Enter Hse No:"))
        self.no_of_members=int(raw_input("Enter No of Members:"))
        self.income=int(raw_input("Enter Income:"))
    def __init__(self,society_name='Surya Apartments', house_no=20 ,no_of_members=3,income=25000,flat='A Type'):
        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.income=income
        self.flat=flat
        
    def allocate_flat(self):

        if self.income>=25000:
            self.flat='A Type'
        elif self.income>=20000:
            self.flat='B Type'
        else:
            self.flat='C Type'
    def display(self):
        print 'Society Name\t:\t',self.society_name ,'\n','House Number\t:\t',self.house_no,'\n','No of Members\t:\t',self.no_of_members,'\n','Flat\t\t:\t',self.flat,'\n','Income\t\t:\t',self.income
    
dat1=SOCIETY()
dat1.display()

print

dat1.input_data()
dat1.allocate_flat()

print dat1.display()
