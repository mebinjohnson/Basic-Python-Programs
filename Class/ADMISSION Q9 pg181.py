class ADMISSION:
    def __init__(self,adno=0,name='',CLASS='',FEES=0):
        self.AD_NO=adno
        self.NAME=name
        self.CLASS=CLASS
        self.FEES=FEES
    def Read_Data(self):
        while True:
            self.AD_NO=int(raw_input("Enter Admission No: "))
            if self.AD_NO in range(10,2000):
                break
            else:
                print "AD_NO Should be in Range 10-2000"
    def __str__(self):
        print 'Ad. No\t:\t',self.AD_NO,'\n','Name\t:\t',self.NAME,'\n','Class \t:\t',self.CLASS,'\n','Fees\t:\t',self.FEES
        
                
        self.NAME=raw_input("Enter Name: ")
        self.CLASS=raw_input("Enter Class: ")
        self.FEES=float(input("Enter Fees: "))
    def Display(self):
        print 'Ad. No\t:\t',self.AD_NO,'\n','Name\t:\t',self.NAME,'\n','Class \t:\t',self.CLASS,'\n','Fees\t:\t',self.FEES




obj1=ADMISSION()

obj1.Read_Data()

