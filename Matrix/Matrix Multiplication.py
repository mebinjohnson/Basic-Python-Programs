matrix1=[]
matrix2=[]
#_________________________________________________________
cnt=1
while True:
    line=raw_input("Enter 1st Matrix ; Row "+str(cnt)+': ')
    cnt+=1
    if not line:
        break
    value=line.split()
    values=[int(values) for values in value]
    matrix1.append(values)
print matrix1
cnt=1
#_________________________________________________________

print '-'*len(matrix1)*50
for x in range (len(matrix1)):
    print '|',
    for y in range(len(matrix1[0])):
        print '\t',matrix1[x][y],'\t',
    print '|'
print '----------------------------------------------------------------------------------------------------------------'


#_________________________________________________________
while True:
    line=raw_input("Enter 2nd Matrix ; Row "+str(cnt)+': ')
    cnt+=1
    if not line:
        break
    value=line.split()
    values=[int(values) for values in value]
    matrix2.append(values)
#_________________________________________________________
#matrix=[[(0)*len(y[0])] for y in range (len(matrix1))]
matrix=[]
for row in xrange(len(matrix1[0])):
    matrix+= [[0]*len(matrix2)]

if len(matrix1[0])==len(matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                matrix[i][j]+=matrix1[i][k]*matrix2[k][j]
    print matrix
else:
    print
    print '<GIVEN MATRIX CANNOT BE MULTIPLIED>'


