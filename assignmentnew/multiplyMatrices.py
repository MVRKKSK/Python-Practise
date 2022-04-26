X = [[14,47,3],
    [12,8,9]]
Y = [[2,8,1,2],
    [6,7,5,5],
    [4,5,6,4]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)