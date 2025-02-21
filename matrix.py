#3Dimentional Matrix multiplication:here i have used nested loops concept:
print("Matrix Multiplication")
x=[[2,3,4],
   [5,7,8],
   [12,54,78]]
y=[[23,3,4],
   [5,18,8],
   [12,5,78]]
z=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for a in range(len(x)):
    for b in range(len(x[0])):
        z[a][b]=x[a][b] * y[a][b]

for final_matrix in z:
    print(final_matrix)