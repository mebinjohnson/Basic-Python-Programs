list=[36,100,67,7,8,9,1]
print 'old list: ',list


print
for i in range(1, len(list)):
    v=list[i]
    j=i
    while (v<list[j-1] and j>=1):
        list[j]=list[j-1]
        j=j-1
        #print list
    #print
        

    list[j]=v
'''

print 'New List: ',list
for i in range(1, len(list)):
    v=list[i]
    j=i
    while (list[i]<list[j-1] and j>=1):
        list[j]=list[j-1]
        j=j-1
    list[j]=v
''' 
print 'New List: ',list
