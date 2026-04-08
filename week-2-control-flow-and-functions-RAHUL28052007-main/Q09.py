# Q09. Functions with Default Parameters
#
# Write the following two functions:
#
#   greet(name, greeting="Hello")
#       Returns the string: "{greeting}, {name}!"
#
#   power(base, exp=2)
#       Returns base raised to exp.
#
# Then in the main block below, call and print:
#   greet("Alice")          → "Hello, Alice!"
#   greet("Bob", "Hi")      → "Hi, Bob!"
#   power(5)                → 25
#   power(2, 10)            → 1024



    # --- YOUR CODE HERE ---
def greet(name, greeting="Hello"):
    return greeting + ", " + name+"!"



    # --- YOUR CODE HERE ---
def power(base, exp=2):
    return base ** exp




    # Call the functions and print results
    # --- YOUR CODE HERE ---
print(greet("Alice"))        
print(greet("Bob", "Hi"))    
print(power(5))              
print(power(2, 10)) 