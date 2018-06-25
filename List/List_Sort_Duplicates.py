list=[79 , 79 , 62 , 85 , 8 , 77 , 86 , 85 , 73 , 72 , 7 , 11 , 3 , 3 , 59 , 48 , 65 , 73 , 87 , 23 , 64 , 14 , 68 , 84 , 98 , 30 , 38 , 66 , 39 , 100 , 97 , 87 , 67 , 50 , 11 , 59 , 20 , 17 , 9 , 80 , 33 , 17 , 60 , 13 , 40 , 3 , 66 , 60 , 26 , 50 , 80 , 99 , 90 , 17 , 7 , 74 , 91 , 33 , 39 , 57]
print len(list)

new_list=[]

list.sort()
print list

for x in range(len(list)-1):
    if list[x]==list[x+1]:
        pass
    else:
        new_list+=[list[x]]
new_list+=[list[(len(list)-1)]]
print len(new_list)
print new_list
