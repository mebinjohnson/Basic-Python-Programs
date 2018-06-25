'''lst=[]
while True:
    element=raw_input('Enter Element: ')
    if element=='':
        break
    
    lst.append(int(element))
'''    
lst=[2,36,100,67,7,8,9,1]
print 'Created List:\t',lst

for x in range(len(lst)):
    if lst[x]%5==0:
        lst[x]=lst[x]/5
    else:
        lst[x]=lst[x]*2

print 'New List:\t',lst


for i in range(len(lst)):
    for j in range (len(lst)-1-i):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp

print 'Sorted List:\t',lst

for i in range(len(lst)):
    for j in range (len(lst)-1-i):
        if lst[j]%2==0:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print 'Even\Odd List:\t',lst
