class student():
    def __init__(self,adno,name,house):
        self.adminno=adno
        self.name=name
        self.house=house
        def display_student(self):
            print "This is a %s %s with %s MPG." %(self.color,self.model,str(self.mpg))
cnt=0
import csv
bfile  = open('Student ID.csv', "rb")
books = csv.reader(bfile)
list2=[]
for row in books:
        obj=student(row[1],row[2],row[5])
        list2.append(obj)
#print list2
