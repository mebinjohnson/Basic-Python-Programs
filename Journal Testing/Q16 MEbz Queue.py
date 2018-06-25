BusQueue = list() # A default queue using list() functon.
rear = front = -1 # Initializing the queue position

#	Inserting element into a queue.
def Insert_Q(BusQueue, rear): 
    Ch = 'Y' 

    while True:
        Ticketno = int(input("Enter ticket no.: "))
        Pname = raw_input("Enter passenger name: ")
        rear += 1 

        Bus = (Ticketno, Pname) # Creating a tuple
        BusQueue.append(Bus) # A tuple added into a list
        print  "Do you want to add more...<y/n>: ",

        Ch = raw_input() 

        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO' or Ch == 'no':
            break 

    return rear 

    #	Removing queue elements 
def Delete_Q(BusQueue, rear):

    Plen = len(BusQueue)   #	Finds total passengers	in bus
    if Plen <= 0:	# Checks	if the bus is empty or	not.
        print ("Bus is empty")	
    else:			

        rear -= 1
        Ticketno, Pname = BusQueue.pop(0)
        # Removing top elements from queue.

        print("Ticket no. %d : Passenger name: %s deleted" % (Ticketno, Pname))
    return rear

# Showing queue elements
def Show_Q(BusQueue, rear):
    front = 0

    Plen = len(BusQueue) # Finds total passengers in bus
    if Plen <= 0:
        # Checks if the bus is empty or not.

        print ("Bus is empty")
    else:

        print ("Passenger information")
        print ("="*46)

        print ("{0:^15} {1:<20}".format("Ticket No.", "Passenger Name"))
        print ("-"*46)

        while front <= rear: # Queue elements processed.
            Ticketno,Pname = BusQueue[front]

            print ("{0:^15} {1:<20}".format(Ticketno, Pname))
            front += 1



while (True):

    front = -1
    print
    print ('P A S S E N G E R	O P E R A T I O N')

    print ('- - - - - - - - - - - - - - - - - - - -')
    print ('1. Insert passenger into bus')

    print ('2. Delete passenger from bus')
    print ('3. Show passenger list')

    print ('4. Exit from operation')

    Opt = int(input( "Enter your option: "))
    print
    if (Opt == 1) :

        # Insert operation of Queue - Adding element at rear of the queue
        rear = Insert_Q(BusQueue, rear)

    elif (Opt == 2) :

        # Delete operation of queue - Deleting element at front of the queue
        rear = Delete_Q(BusQueue, rear)
    elif (Opt == 3) :

        # Traversing/Showing queue element
        Show_Q(BusQueue, rear)

    elif (Opt == 4) :
        break
    raw_input()
