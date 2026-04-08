# Q03. Multiplication Table (for loop)
#
# Ask the user for a positive integer n.
# Print its multiplication table from 1 to 10.
#
# Sample Input:   Enter a number: 5
# Sample Output:
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
#   5 x 10 = 50

# --- YOUR CODE HERE ---
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)