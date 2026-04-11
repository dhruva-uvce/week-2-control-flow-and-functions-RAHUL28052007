# Q10. Call by Reference — List Mutations
#
# Write the following two functions:
#
#   add_element(lst, element)
#       Appends element to lst in-place. Returns nothing.
#
#   double_elements(lst)
#       Multiplies every element in lst by 2 in-place. Returns nothing.
#
# Then in the main block:
#   1. Create numbers = [1, 2, 3]
#   2. Call add_element(numbers, 4) and print the list  → [1, 2, 3, 4]
#   3. Call double_elements(numbers) and print the list → [2, 4, 6, 8]



    # --- YOUR CODE HERE ---
def add_element(lst, element):
    lst.append(element)


def double_elements(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2  
