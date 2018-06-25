class bus():
    def __init__(self):
        self.name=''
        self.ticket_number=0

    def insert(self):
        self.name=raw_input("Enter Name of Passenger\t:\t").upper()
        self.ticket_number=raw_input("Enter Passenger TIcket Number\t:\t")

def main(bus_queue):
    print '-'*150
    print "\t\t\tP A S S E N G E R          O P E R A T I  O N"
    print '-'*150
    
    functions=['Insert Passenger','Remove Passenger','View All Passengers','Exit']
    
    for x in range (len(functions)):
        print '\t[',x+1,']',functions[x]
    print '-'*150
    selection=int(input("Enter Selection\t:\t"))
    print
    print '-'*150
    print
    if selection==1:
        while True:
            ch='y'
            obj=bus()
            obj.insert()
            bus_queue.append(obj)
            choice=raw_input("Do you want to add more passengers\t(Y/N):\t").upper()
            if choice in ['NO','N']:
                break
    elif selection==2:
        removed_passenger=bus_queue.pop(0)
        print 'Passenger: ',removed_passenger.name,'\nTicket Number: ',removed_passenger.ticket_number,'\n\tHAS BEEN SUCCESFULLY REMOVED FROM BUS'
    elif selection==3:
        if len(bus_queue)!=0:
            for passenger in bus_queue:
                    print passenger.name,passenger.ticket_number
        else:
            print 'No Passengers in Bus'
    elif selection==4:
        exit()
    print '-'*150
        
    raw_input()

bus_queue=[]      
while True:
    main(bus_queue)
        
        
