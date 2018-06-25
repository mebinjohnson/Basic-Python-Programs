no=int(input("Enter the number to Check Prime/Non-Prime: "))

res=0
for x in range (2,no):
    for y in range(2,x):
        if no%y==0:
            res=1
            break

if res==1:
    print no, "is a NOT a Prime No"

else:
    print no,"is a Prime No"
    
