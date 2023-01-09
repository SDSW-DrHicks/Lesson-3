# ----------------------------------------------
# Nested Loops
# ----------------------------------------------

# Here is the general structure of a nested set of loops:

# outer for loop
#for element in sequence
#   # inner for loop
#   for element in sequence:
#       body of inner for loop
#   body of outer for loop

# Example: Generate a multiplication table

# outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()
