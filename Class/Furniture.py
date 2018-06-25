class Furniture:
    def __init__(self,fcode=0,ftype='',comp='',loc=''):
        self.__Fcode=fcode
        self.__Ftype=ftype
        self.__Company=comp
        self.__Location=loc
    def Get_Location(self):
        if self.__Ftype=='Dinning Table Set':
            self.__Location='India'
        elif self.__Ftype=='Bedroom Set':
            self.__Location='Malaysia'
        else:
            self.__Location='UAE'
    def Input(self):
        self.__Fcode=int(input("Enter Furniture Code: "))
        self.__Company=raw_input("Enter Company Name: ")
        print
        print "Ftype :"
        ftype=['Dinning Table Set','Bedroom Set','Sofa Set']
        for x in range (len(ftype)):
            print 'Enter',x+1, 'for - ',ftype[x]
        y=int(input("Enter selection: "))
        if y==1:
            print 1
            self.__Ftype='Dinning Table Set'
        elif y==2:
            print 2
            self.__Ftype='Bedroom Set'
        else:
            print 3
            self.__Ftype='Sofa Set'
        self.Get_Location()
    def Output(self):
        print "Furniture Code: \t",self.__Fcode
        print "Furniture Type: \t",self.__Ftype
        print "Company Name: \t",self.__Company
        print "Location: \t",self.__Location
obj=Furniture()
obj.Input()
#obj.Get_Location()
obj.Output()
