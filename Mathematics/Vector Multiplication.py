def create_vector():
    vector1=[0,0,0]
    vector1[0]=int(input('Enter i^ :'))
    vector1[1]=int(input('Enter j^ :'))
    vector1[2]=int(input('Enter k^ :'))
    return vector1
def dot_product(vector1,vector2):
    product=0
    for x in range(3):
        product+=vector1[x]*vector2[x]
    return product
def scalar_product(vector1,vector2):
    result=[0,0,0]
    result[0]=vector1[1]*vector2[2]-vector2[1]*vector1[2]
    result[1]=-(vector1[0]*vector2[2]-vector2[0]*vector1[2])
    result[2]=vector1[0]*vector2[1]-vector2[0]*vector1[1]
    return result
        
def display_vector(vector):
    print vector[0],'i^ + ',vector[1],'j^ + ',vector[2],'k^'

def main():
    while True:
        print '---------------VECTOR CALCULATOR---------------'
        print '\t1. Add Vectors:'
        print '\t2. View Vectors:'
        print '\t3. Find Dot Product'
        print '\t4. Find Cross Product:'
        print
        vector1=[-1,-8,2]
        vector2=[1,1,1]
        selection=int(input("Enter Selection: "))
        if selection==1:
            
            vector1=create_vector()
            vector2=create_vector()
        elif selection==2:
            print 'Vector 1: ',
            display_vector(vector1)
            print
            print 'Vector 2: ',
            display_vector(vector2)

        elif selection==3:
            print "Dot Product: ",dot_product(vector1,vector2)
        elif selection==4:
            print "Scalar Product: ",display_vector(scalar_product(vector1,vector2))
        else:
            print 'Wrong Choice'
        raw_input()

while True:
    try:
        main()
    except SyntaxError:
        print 'Wrong Input'
        continue
     

