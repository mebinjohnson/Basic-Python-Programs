read_file=open('data.txt','rb')
string=''

string=read_file.read()

read_file.close()

upper=''
lower=''
other=''

print string

for letter  in string:
    #if letter.isalpha():
    if letter.isupper():
            upper+=letter
    elif letter.islower():
            lower+=letter
    else:
        other+=letter

print 'Upper=',upper
print 'Lower=',lower
print 'Other=',other


upper_file=open("upper.txt",'wb')
lower_file=open("lower.txt",'wb')
other_file=open('other.txt','wb')

upper_file.write(upper)
lower_file.write(lower)
other_file.write(other)

upper_file.close()
lower_file.close()
other_file.close()











        
        
