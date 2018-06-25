print '~'*80
print '*'*80
print '    '*8,'PhoneBook','    '*5
print '*'*80
print '~'*80
n=int(input("Enter total: "))


phonebook={}
i=1

while i<=n:
    name=raw_input("Enter name : ")
    no=raw_input("Enter Numb: ")
    phonebook[name]=no
    i+=1


sname=raw_input("Enter Name to Search: ")

n=1
for x in phonebook.keys():
    if cmp(x,sname)==0:
        print x,'\t-\t',phonebook[x]
        n=0

if n==1:
        print "Name do not Exist"
raw_input()

