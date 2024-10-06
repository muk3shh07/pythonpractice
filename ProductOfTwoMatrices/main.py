def matrix(m,n):
    o = []
    for i in range (m):
        row = []
        for j in range(n):
            inp = input(f"Enter  O[{i}][{j}]")
            row.append(inp)
        o.append(row)
    return o

def product(A,B):
    output = []
    for i in range(len(output)):
        rows = []
        for j in range(len(output[0])):
            for k in range(len(B)):
                output[i][j] += A[i][k] * B[k][j]

m = int(input("Enter no of rows::"))
n = int(input("Enter no. of columns::"))

print("Enter the matrix A")
A = matrix(m,n)

print("Enter the matrix B")
B = matrix(m,n)

p=product(A,B)

print(p)

