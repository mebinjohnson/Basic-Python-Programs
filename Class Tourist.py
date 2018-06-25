class Tourist(object):
    def __init__(self,Type,Distance,Carno,Origin,Destination):
        self.Type=Type
        self.Distance=Distance
        self.Carno=Carno
        self.Origin=Origin
        self.Destination=Destination
        self.CalcCharge()
    def CalcCharge(self):
        if self.Type=='E':
            self.charge=16*self.Distance
        elif self.Type=='A':
            self.charge=22*self.Distance
        else:
            self.charge=30*self.Distance

    def Enter(self):
        
        self.Carno=int(raw_input("Enter Carno:"))
        self.Origin=raw_input("Enter Origin: ")
        self.Destination=raw_input("Enter Dewstiantion: ")
        self.CalcCharge()

    def Show(self):
        print (self.Type,self.Distance,self.Carno,self.Origin,self.Destination)
        print 'Charge: ',self.charge,'\t'
        
    
obj1=Tourist('E',250,11,'Uganda','DXB')
#obj1.Enter()
obj1.Show()

obj2=Tourist('L',250,12,'Iran','UAE')
#obj2.Enter()
obj2.Show()

obj3=Tourist('L',250,13,'INdia','DXB')
#obj3.Enter()
obj3.Show()

'''
obj1=Tourist('E',250)
obj1.Enter()
obj1.Show()
'''
list=[obj1,obj2,obj3]


snum=int(raw_input("Enter no. to search: "))

for x in list:
    if x.Carno==snum:
        x.Show()








