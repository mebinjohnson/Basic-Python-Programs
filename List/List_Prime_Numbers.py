list=[79 , 79 , 62 , 85 , 8 , 77 , 86 , 85 , 73 , 72 , 7 , 11 , 3 , 3 , 59 , 48 , 65 , 73 , 87 , 23 , 64 , 14 , 68 , 84 , 98 , 30 , 38 , 66 , 39 , 100 , 97 , 87 , 67 , 50 , 11 , 59 , 20 , 17 , 9 , 80 , 33 , 17 , 60 , 13 , 40 , 3 , 66 , 60 , 26 , 50 , 80 , 99 , 90 , 17 , 7 , 74 , 91 , 33 , 39 , 57]
new_list=[]
for x in range(len(list)):
    for a in range(2,x):
        if x%a==0:
            break
    else:
        new_list+=[x]

print new_list