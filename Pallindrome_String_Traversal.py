string=raw_input("Enter String to check for Pallindrome: ")
rev=''
for x in range(len(string)-1,-1,-1):
    rev+=string[x]

if rev==string:
    print string,'is a Pallindrome'
else:
    print string,'is not a Pallindrome'
