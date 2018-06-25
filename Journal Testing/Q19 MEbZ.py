import pickle
class Student():
  def __init__(self,roll=0,name='',marks=0):
    self.rollno=roll
    self.name=name
    self.marks=marks
  def add(self):
    self.rollno=int(input("Enter Roll No:"))
    self.name=(raw_input("Enter Name:")).upper()
    self.marks=int(raw_input("Enter Marks:"))
  def display(self):
    print 'Roll No:\t',self.rollno
    print 'Name:\t',self.name
    print 'Marks:\t',self.marks

def save(obj):
  f=open('student_data.log','ab+')
  pickle.dump(obj,f)
  f.close()
def open_data():
  f=open('student_data.log','rb+')
  data_list=[]
  try:
    while True:
      obj=pickle.load(f)
      data_list.append(obj)
  except EOFError:
    f.close()
    print '\t\t\t\t\t<DATA READ>'
  return data_list


def main():
  print '_'*80
  print "\t\tSTUDENT MARK DATABASE"
  print '_'*80
  print '\t1.Add New Record'
  print '\t2.Search by Roll Number'
  print '\t3.Search by Name'  
  print '\t4.Display All Records'
  print '\t5.Exit'
  print '-'*50
  print 

  option=int(raw_input("Enter Choice: "))
  print '_'*75
  if int(option)==1:
    obj=Student()
    obj.add()
    save(obj)
  elif int(option)==2:
    no=int(raw_input("Enter Student Roll No to Search: "))
    s=0
    data_list=open_data()
    for x in data_list:
      if x.rollno==no:
        x.display()
        s=1
    if s!=1:
      print "\t<RECORD NOT FOUND>"
  elif int(option)==3:
    name=raw_input("Enter Student Name to Search: ")
    s=0
    data_list=open_data()
    for x in data_list:
      if x.name==name.upper():
        x.display()
        s=1
    if s!=1:
      print "\t<RECORD NOT FOUND>"
  elif int(option)==4:
    print 'DISPLAYING ALL RECORDS'
    print '.............................................'
    data_list=open_data()
    print
    for x in data_list:
      x.display()
      print '-'*50
      print
      s=1
    if s!=1:
      print "\t<NO RECORD FOUND>"
  elif int(option)==5:
    exit()
  else:
    print "\t<WRONG CHOICE>"
  raw_input()

while True:
  main()
      
    
    
    
