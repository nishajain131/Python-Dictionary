# In this pgm, for all multiples of three will tell fizz and then multiples of five will tell buzz and multiples of three and five will be fizzbuzz!
#If its neither divisible by 3 nor 5 then we print the num

for num in range(1,51):
    if (num%3==0 & num%5==0):
        print("fizzbuzz")
    elif (num%3 == 0):
        print("fizz")
    elif (num%5==0):
        print("buzz")
    else :
        print(num)