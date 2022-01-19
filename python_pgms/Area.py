# This pgm takes a single line input as length and breadth and prints area of rectangle

l,b = list(map(int,input().split()))
print(l,b)
print("Area of rectangle is " + str(l*b))
