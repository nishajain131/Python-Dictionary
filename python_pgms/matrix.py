#Given two integers r and c, indicating the number of rows and columns, 
#print a two-dimensional matrix such that the elements of the matrix are in an increasing sequence 
# from 1 to rXc, in a row-major order.

r = 8
c = 8
a=1
for i in range(1,r+1):
    for j in range(1,c+1):
        print(a,end=" ")
        a+=1
    print()
