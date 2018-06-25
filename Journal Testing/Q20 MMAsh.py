import os
# Program to multiply two matrices using nested loops
# 3x3 matrix
X = [  [5,4,6],     [2 ,5,8],      [3 ,1,4]]
# 3x4 matrix

Y = [[8,7,3,4],    [3,5,3,4],    [5,6,3,4]]

# result is 3x4
print len(Y)

print len(Y[0])

result = [[0,0,0,0],         [0,0,0,0],          [0,0,0,0]  ]

# iterate through rows of X

for i in range(len(X)):
   
   # iterate through columns of Y
   for j in range(len(Y[0])):
                
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
raw_input()
