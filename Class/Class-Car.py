class Car(object):
    condition="new"
    def __init__(self,model,color,mpg):
        self.model=model
        self.color=color
        self.mpg=mpg

    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color,self.model,str(self.mpg))

my_car=Car("delorean", "silver", 88)

#print my_car.model
#print my_car.color
#print my_car.mpg
my_car.display_car()
