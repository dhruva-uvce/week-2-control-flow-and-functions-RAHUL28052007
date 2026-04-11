# Q07. Reverse a Number (while loop)
#
# Ask the user for a positive integer.
# Print the reverse of the number using a while loop.
#
# Sample Input 1:   Enter a number: 1234
# Sample Output 1:  Reversed: 4321
#
# Sample Input 2:   Enter a number: 5000
# Sample Output 2:  Reversed: 5

# --- YOUR CODE HERE ---
def reverse_number(n):
    if n == 0:
        return 0
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev