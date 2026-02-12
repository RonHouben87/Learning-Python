#_____OPTION 1_____

print("Welcome to FizzBuzz!")

# Declaring the function
def fizzbuzz(n):
    if (n % 3 == 0 and n % 7 == 0):
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    elif "3" in str(n):   # check for number 3 in the str(int())
        return "Almost Fizz"
    else:
        return n
        
# Input from user
limit = int(input())

# Play FizzBuzz
for i in range(1,limit + 1):
    result = fizzbuzz(i)
    print(result)

#_____OPTION 2_____

print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        if "3" in str(number):
            result = "Almost Fizz"
        else:
            result = str(number)
    return result

limit = int(input())

# Play FizzBuzz
for i in range(1, limit + 1):
    print(fizzbuzz(i))
