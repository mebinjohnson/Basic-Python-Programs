class Furniture:
    def __init__(self,fcode=101,ftype='dinning table',comp="IKEA",loc='Null'):
        self.__Fcode=fcode
        self.__Ftype=ftype
        self.__Company=comp
        self.__Location=loc
        
    def GetLocation(self):
        if self.__Ftype=="dining tabe":
            self.__Location='India'
        elif self.__Ftype=='bedroom set':
            self.__Location='Malaysia'
        else:
            self.__Location='UAE'

    def input(self):
        self.__Fcode=int(input("Enter Fcode: "))
        self.__Ftype=raw_input("Enter Ftype: ")
        self.__Company=raw_input("Enter Company :")
        self.GetLocation()

    def output(self):
            print self.__Fcode,self.__Ftype,self.__Company,self.__Location

x=Furniture()
x.input()
x.output()
