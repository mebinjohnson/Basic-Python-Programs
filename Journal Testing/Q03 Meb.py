import math 

while (True):

    Area = 0 

    print

    print ("1. Area of a circle") 

    print ("2. Area of a rectangle") 

    print ("3. Area of a square")
    print ("4. Quit")

    Opt = int(input( "Enter your option: "))
    if (Opt == 1) :

        r = float(input("Enter radius of the circle: "))
        Area = round(math.pi, 2) * r * r

        print("Area of the circle is => %.2f" % Area)
    elif (Opt == 2) :

        length = float(input("Enter length of the rectangle: "))
        breadth = float(input("Enter breadth of the rectangle: "))
        Area = length * breadth

        print("Area of the rectangle is => %.2f" % Area)
    elif (Opt == 3) :

        side = float(input("Enter side of the square: "))
        Area = side * side

        print("Area of the square is => %.2f" % Area)
    if (Opt == 4):
        exit()
