def linear_search(lst,size,item):
    flag=0
    for i in range(size):
        if lst[i]==item:
            flag=1
            print item," present at position ",i+1
    if flag==0:
        print item," is not present in the list"

def binary_search(lst,size,item):
    flag=0
    beg=0
    end=size-1
    while beg<end:
        mid=int((beg+end)/2)
        if item==lst[mid]:
            flag=1
            print item," present at position ",mid+1
            return
        elif lst[mid]<item:
            beg=mid+1
        else:
            end=mid-1
    if flag==0:
        print item," is not present in the list"

def main():
    while True:

        print

        print("Main Menu: Searching")
        print("------------------")
        print("1 - Linear Searching")
        print("2 - Binary Searching")
        print("3 - Quit")
        print("------------------")
        opt=input("Enter you choice: ")
        if opt==1:
            lst=[]
            size=input("enter the size of list-1:")
            for i in range(size):
                ele=input("Enter the element :")
                lst.append(ele)
            item=input("Enter the element to search:")
            linear_search(lst,size,item)
        elif opt==2:
            lst=[]
            size=input("enter the size of list-1:")
            for i in range(size):
                ele=input("Enter the element :")
                lst.append(ele)
            lst.sort()
            print lst
            item=input("Enter the element to search:")
            binary_search(lst,size,item)
        elif opt==4:
            print "Exiting.................."
            exit()


main()
