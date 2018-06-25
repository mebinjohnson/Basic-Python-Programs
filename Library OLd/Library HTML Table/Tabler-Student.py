from Functions import *
data=''
x='<htm><body><table border="8">'
data+=x

list=open_student()


data+='<td>'+'ADMIN NO.'+'</td>'+'<td>'+'NAME'+'</td>'+'<td>'+'CLASS'+'</td>'+'<td>'+'SECTION'+'</td>'+'<td>'+'HOUSE'+'</td>'


for i in range (len(list)):
    data+= '<tr>'+'<td>'+list[i][0]+'</td>'+'<td>'+list[i][1]+'</td>'+'<td>'+list[i][4]+'</td>'+'<td>'+list[i][5]+'</td>'+'<td>'+list[i][6]+'</td>'+'</tr>'

data+='</table></body></html>'

design('*',25)
design('Viewing All Student Records')
design('*',25)


print "HTML Created"

ofile  = open('Student Table.htm', "w")

for lines in data:
    ofile.write(lines)


import os
os.startfile("Student Table.htm")


menu_end()
