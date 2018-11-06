for num in range(1,51):
    if num % 15 == 0:
        print(str(num) + " is a FizzBuzz number!!!")
    elif num % 5 == 0:
        print(str(num) + " is a Buzz number!")
    elif num % 3 == 0:
        print(str(num) + " is a Fizz number!")
    else:
        print num

