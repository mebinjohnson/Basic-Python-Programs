list1=[15,10,12,21,52,76]
list2=[23,41,67,83,13,53]


for x in range(len(list1)):
    if x%2!=0:
        a=list1[x]
        list1[x]=list2[x]
        list2[x]=a
print list1,
print list2,
