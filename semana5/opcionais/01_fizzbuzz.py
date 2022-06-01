def fizzbuzz(n):
    if (n%3 == 0 and n%5 ==0):
        output = "FizzBuzz"
    elif (n%3 == 0):
        output = ("Fizz")
    elif (n%5 == 0):
        output = "Buzz"
    else:
        output = n
    return output