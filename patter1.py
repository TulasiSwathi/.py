# Define the number of rows
num_rows = 3

# Loop through rows
for i in range(num_rows):
    # Print spaces before the first asterisk
    print(" " * (i * 11), end="")

    # Print the first asterisk
    print("*", end="")

    # Print spaces between the first and second asterisk
    print(" " * (20 - 11 * i), end="")

    # Print the second asterisk
    if i != num_rows - 1:
        print("*", end="")

    # Move to the next line after each row
    print()
