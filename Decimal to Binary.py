hd='''
                                                                                                                Decimal
                                                                                                                      to
                                                                                                        Binary Converter
________________________________________________________________________________
'''

print hd

#______________________________________________________________________________________________________________________________________________________________________

num=int(input("Enter Value : "))
print

m=''
for x in range (num):
    print '2|',num,'\t|',num%2
    m+=str(num%2)
    num=num//2
    if num<=0:
        break
binary=''
for x in range (len(m)-1,-1,-1):
    binary+=m[x]


print '\nBinary : ' , binary
input
