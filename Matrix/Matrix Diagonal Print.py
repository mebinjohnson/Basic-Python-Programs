matrix=[[1,6,9],[7,9,7],[1,5,6]]
sum=0
for x in range(len(matrix)):
    for y in range (len(matrix[0])):
                   print matrix[x][y],
    print



for x in range (len(matrix)):
    for y in range (len(matrix[0])):
        if x==y:
            print matrix[x][y],
            sum+=matrix[x][y]
        else: print 0,
    print

print sum

for x in range(len(matrix)):
    for y in range (len(matrix[0])-1,-1,-1):
                   print matrix[x][y],
    print
