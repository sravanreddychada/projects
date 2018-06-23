# take input from the user
try:
    num = int(input(">>> Enter a number greater than 1 : "))
# prime numbers are greater than 1
    if num > 1:
# check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
# if input number is less than 1 , it is not valid number
    else:
        print(num, "is not a valid number")
except ValueError:
        print("Please provide valid integers")