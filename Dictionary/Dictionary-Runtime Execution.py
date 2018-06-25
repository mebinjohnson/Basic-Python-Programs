winners={}


n=int(input("Enter the Number of Students: "))

for a in range (n):
    key=raw_input("Enter Name: ")
    value=int(input("Enter no of compet: "))
    winners[key]=value

print winners
