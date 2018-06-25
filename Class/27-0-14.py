class A(object):
    var=0
    def __init__(self):
        A.var+=1      #Class Variable
        self.var+=1 #Instance Variable
        


A()
print A.var
