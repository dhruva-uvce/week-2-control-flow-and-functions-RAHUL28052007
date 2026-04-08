# Q05. FizzBuzz (for loop + if-else)
#
# Ask the user for a positive integer n.
# Print all numbers from 1 to n, but:
#   - For multiples of 3, print "Fizz" instead of the number
#   - For multiples of 5, print "Buzz" instead of the number
#   - For multiples of both 3 and 5, print "FizzBuzz"
#
# Sample Input:   Enter n: 15
# Sample Output:
#   1
#   2
#   Fizz
#   4
#   Buzz
#   ...
#   FizzBuzz

# --- YOUR CODE HERE ---
n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
