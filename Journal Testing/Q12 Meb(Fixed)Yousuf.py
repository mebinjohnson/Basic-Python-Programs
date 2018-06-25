def  bubble_sort(lst,size):
    
    for i in range(1,size):
        print "\nIteration:",i
        for j in range(0,size-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
        for k in lst:
            print k,


def select_sort(lst,size):
    for i in range(size-1):
        print "\nIteration:",i+1
        small=lst[i]
        for j in range(i+1,size):
            if small>lst[j]:
                pos=j
                small=lst[j]
                temp=lst[pos]
                lst[pos]=lst[i]
                lst[i]=temp
        for k in lst:
            print k,

def  insert_sort(lst,size):
    for i in range(1,size):
        print "\nIteration:",i
        temp=lst[i]
        pos=i-1
        while pos>=0 and lst[pos]>temp:
            lst[pos+1]=lst[pos]
            pos-=1
            lst[pos+1]=temp
        for k in lst:
            print k,





def  main():
    while True:
        print
        print("Main Menu: Sorting")
        print("------------------")
        print("1 - Bubble Sorting")
        print("2 - Selection Sorting")
        print("3 - Insertion Sorting")
        print("4 - Quit")
        print("------------------")
        opt=input("Enter you choice: ")
        if opt==1:
            lst=[]
            size=input("Enter the size of list-1:")
            for i in range(size):
                ele=input("Enter the element :")
                lst.append(ele)
            bubble_sort(lst,size)

        elif opt==2:
            lst=[]
            size=input("enter the size of list-1:")
            for i in range(size):
                ele=input("Enter the element :")
                lst.append(ele)
            select_sort(lst,size)
        elif opt==3:
            lst=[]
            size=input("enter the size of list-1:")
            for i in range(size):
                ele=input("Enter the element :")
                lst.append(ele)
            insert_sort(lst,size)
        elif opt==4:
            print "Exiting.................."

main()

