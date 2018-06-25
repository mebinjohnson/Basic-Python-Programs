class  myclass():
    def __init__(self,val=0):
        self.L=[]
        for i in range(val):
            self.L.append(i)
    def __str__(self):
        return 'L:%s'%(str(self.L))
    def method1(self,x=0):
        for i in range(len(self.L)):
            self.L[i]=x*self.L[i]
        return self.L
    def method2(self,i=0):
        if i in range (len(self.L)):
            return self.L[i]
        else:
            return None

inst1=myclass()
print inst1

inst2=myclass(3)
print inst2

print inst2.method1(2)

print inst2.method2(1)
