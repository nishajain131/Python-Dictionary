#Given an integer input 'n', print a number triangle of n lines

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()