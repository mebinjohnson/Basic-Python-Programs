from Functions import *
data=''
x='<htm><body><table border="10">'
data+=x

list=open_book()


data+='<td>'+'BOOK NO.'+'</td>'+'<td>'+'NAME'+'</td>'+'<td>'+'AVAILIBILITY'+'</td>'+'<td>'+'ISSUED BY'+'</td>'


for i in range (0,len(list)):
    if list[i][2]=='y':
        a="Available"
    else:
        a="Issued"
    if list[i][3]==',':
        b='Null'
    else:
        b=list[i][3]
    data+= '<tr>'+'<td>'+list[i][0]+'</td>'+'<td>'+list[i][1]+'</td>'+'<td>'+a+'<td>'+b+'</td>''</tr>'

data+='</table></body></html>'

design('*',25)
design("Viewing All Books")
design('*',25)
print "HTML Created"

ofile  = open('Book Table.htm', "w")

for lines in data:
    ofile.write(lines)
        
import os
os.startfile("Book Table.htm")


menu_end()
