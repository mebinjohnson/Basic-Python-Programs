class Circle:
    total_circles=0
    pi=22.0/7.0
    all_circles=[]
    def __init__(self,r=1.0):
        self.radius=r
        self.area=0
        Circle.all_circles.append(self.radius)
        #Circle.calc_area(self)
        self.calc_area()
        
    def calc_area(self):
        self.area=Circle.pi*(self.radius**2.0)
        Circle.total_circles+=1
        return self.area
    def __str__(self):
        return "Radius: "+str(self.radius)+"        ;       Area: "+str(self.area)


c1=Circle(2)
c2=Circle(3)

#c1.calc_area()

print c1
print Circle.total_circles,'\n',Circle.all_circles
