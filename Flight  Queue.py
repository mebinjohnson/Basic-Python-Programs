Plane_Queue=[]
rear=front=-1

def Insert_Q(Plane_Queue,rear):
    ch='y'
    while True:
        flghtno=raw_input("Enter Flight Number: ")
        dest=raw_input("Enter Destination of Flight: ")
        rear+=1

        flight=flghtno,dest
        Plane_Queue.append(flight)
        sel=raw_input('Do you want add more records y/n: ')

        if sel in ['no','n','No','NO','N']:
            break

    return rear

def Delete_Q(Plane_Queue,rear):
    if len(Plane_Queue)==0:
        print 'Plane_Queue Empty'
    else:
        rear-=1
        flghtno,dest=Plane_Queue.pop()
        print 'Flight Number: ',flghtno,'\nDestination :',dest,' was deleted'

    return rear

def Show_Q(Plane_Queue,rear):
    if len(Plane_Queue)==0:
        print "Queue Empty !!!"

    else:
        print '*'*45
        print "Flight Information"
        print '*'*45
        print 'Flight No.           |            Destination'
        for x in range (len(Plane_Queue)):
            (fno,dest)=Plane_Queue[x]
            #print fn0,'                             |                                         ',dest
            print Plane_Queue[x]

def main():
    print
    print  '-'*100
    print 'F L I G HT       O P E R A T I O N'
    print  '-'*100
    functions=['Insert Flight Information','Delete Flight from Queue','Show All Flight in Queue','Exit']
    for x in range (len(functions)):
        print '[',x+1,']        ',functions[x]
    sel=int(input("Enter Selection: "))
    if  sel==1:
        Insert_Q(Plane_Queue,rear)
    elif sel==2:
        Delete_Q(Plane_Queue,rear)
    elif sel==3:
        Show_Q(Plane_Queue,rear)
    elif sel==4:
        exit()
    else:
        print 'Wrong Choice'
    raw_input()

while True:
    try:
        main()
    except IOError:
        print "Wrong Input"

