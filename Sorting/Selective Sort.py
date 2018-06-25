list=[2,36,100,67,7,8,9,1]
list=[40,67,-23,11,27,38,-1]

print 'Old List:\t ',list
'''
for i in range (len(list)):
    small=list[i]
    pos=i
    for j in range (len(list)):
        if list[j]>small:
            pos=j
            temp=list[i]
            list[i]=list[pos]
            list[pos]=temp
        print list
'''

for i in range (len(list)):
    for j in range (len(list)):
        if list[j]>list[i]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
    print list
print 'Sorted List:\t',list
