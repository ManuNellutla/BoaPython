# fizz Buzz algorithm
# if a number is divisible by 3 print 'Fizz'
# if a number is divisible by 5 print 'Buzz'
# if a number is divisible by both 3 and 5 print 'FizzBuzz'
# else print number.

for a in range(1,20):
    result = ""
    if a % 3 == 0:
        result += "Fizz"
    if a % 5 == 0:
        result += "Buzz"

    if a % 3 != 0 and a % 5 != 0:
        result = str(a)
    print(result)
