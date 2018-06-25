theList = list() # Creating a default list/array

# Adding element into array def createList(theList):

ctr = 1
Ch = 'Y'
while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':

    print ("Enter number %d	" % (ctr))

    val = float(input("Enter value:"))	

    theList.append(val)	#	adding number into list

    print	("Do you want	to add more...<y/n>: ")

    Ch = raw_input()
    ctr += 1

    if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
        break

# Delete first element

def deleteAtBeginning(theList):
    ctr = len(theList)

    if ctr > 0:
        delVal = theList.pop(0) # delete first (0th) element print ("Deleted value is:", delVal)
    else:
        print ("List is empty")

# Delete by value

def DeleteByValue(theList, delVal):
    Flag = 0

    for i in range(len(theList)):
        if theList[i] == delVal:
            del (theList[i])
            Flag = 1

                #break

        if Flag == 0:
            print("Element does not found in list")

        else:
            print("Successfully deleted:", delVal)

# Delete at end

def deleteAtEnd(theList):
    ctr = len(theList)

    if ctr > 0:
        delVal = theList.pop() # delete last element

        print ("Deleted value is:", delVal)

    else:
        print ("List is empty")

# Show array elements

def show_element(theList):
    ctr = len(theList)

    if ctr > 0:
        print("The array is:...")

        for i in range(0, len(theList)):

            print(theList[i],)

    else:

        print ("List is empty")



Opt = 0

while (True):
    print()
    print (' M A I N M E N U')
    print('- - - - - - - - - -')
    print ('1. Create a list')
    print ('2. Delete at beginning')
    print ('3. Delete by number/value')
    print ('4. Delete at end')
    print ('5. Show elements')
    print ('6. Quit')
    print ('- - - - - - - - - -')

    Opt = int(input( "Enter your option: "))
    print()

    if (Opt == 1) :
        createList(theList)

    elif (Opt == 2) :
        deleteAtBeginning(theList)

    elif (Opt == 3) :
        delVal = input("Enter the value which you want to delete: ")
        DeleteByValue(theList, delVal)

    elif (Opt == 4) :
        deleteAtEnd(theList)

    elif (Opt == 5) :
        show_element(theList)

    elif (Opt == 6) :
        break


