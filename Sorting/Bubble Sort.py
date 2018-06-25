lst=[40,67,-23,11,27,38,-1]
print ' List:\t',lst

for i in range(len(lst)):
    for j in range (len(lst)-1-i):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
    print lst

print 'Sorted List:\t',lst
