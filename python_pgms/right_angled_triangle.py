#Checks if a triangle is right angled

a,b,c = list(map(float,input().split()))
if ((a*a == (b*b)+(c*c)) or (b*b == (a*a)+(c*c)) or (c*c == (b*b)+(a*a))):
    print("Yes")
else:
    print("NO")