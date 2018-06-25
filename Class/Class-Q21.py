
class ITEMINFO(object):
    def __init__(self,ICode=0,Item='Null',Price=0,Qty=0):
        self.ICode=ICode
        self.Item=Item
        self.Price=Price
        self.Qty=Qty
        self.Discount=0
        self.Netprice=0
    def FindDisc(self):
        if self.Qty<=10:
            self.Discount=0
        elif self.Qty<=20:
            self.Discount=self.Price/100*10
        else:
            self.Discount=self.Price/100*15
        self.Netprice=self.Price*self.Qty-self.Discount
        
    def Buy(self):
        self.ICode=raw_input("Enter Item Code: ")
        self.Item=raw_input("Enter Item Name: ")
        self.Price=float(raw_input("Enter Price of Item: "))
        self.Qty=int(raw_input("Enter Quantity: "))
        self.FindDisc()
        
    def ShowAll(self):
        print '\nItem Code\t:\t',self.ICode,'\nItem\t:\t',self.Item,'\nPrice\t:\t',self.Price,'\nQuantity\t:\t',self.Qty,'\nDiscount\t:\t',self.Discount,'\nNet Price\t:\t',self.Netprice,' AED',


dat=ITEMINFO(1155411005,'Asus S550CB',3799,100)
dat.FindDisc()
dat.ShowAll()

print

dat1=ITEMINFO(0,0,0,0)
dat1.Buy()
dat1.ShowAll()

