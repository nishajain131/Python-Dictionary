# This program prints multiplication table of a number entered by user

num = int(input("Enter a number "))

for i in range(1,11):
    print(str(num) + " x " + str(i) + " is " + str(i*num))

