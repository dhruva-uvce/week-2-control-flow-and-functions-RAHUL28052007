# Q04. Star Pattern (nested for loop)
#
# Ask the user for a positive integer n.
# Print a right-angled triangle of '*' with n rows.
#
# Sample Input:   Enter number of rows: 5
# Sample Output:
#   *
#   **
#   ***
#   ****
#   *****

# --- YOUR CODE HERE ---
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()