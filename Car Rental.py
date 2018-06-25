import pickle
class rental:
    def __init__(self,name='',model='',year=0,price=0):
        self.name=name
        self.model=model
        self.year=year
        self.price=price
    def add(self):
        self.name=raw_input("Enter Vehicle Maker: ").upper()
        self.model=raw_input("Enter Vehicle Model: ").upper()
        self.year=int(raw_input("Enter Vehicle Year: "))
        self.price=int(raw_input("Enter Vehicle Price: "))
    def __str__(self):
        return         str(self.name)+str(self.model)+str(self.year)+str(self.price)

def save(data):
    f=open("Data.log",'wb+')

    for obj in data:
        pickle.dump(obj,f)
    f.close()

def open_data():
    f=open("Data.log",'rb+')
    data=pickle.load()
    return data
def view_all(data):
    for x in data:
        print x
def main(data):
    sel=int(input("Enter sel: "))
    if sel==1:
        obj=rental()
        obj.add()
        data.append(obj)
        save(data)
    elif sel==2:
        view_all(data)
datal=[]
while True:
    main(datal)
        
    
