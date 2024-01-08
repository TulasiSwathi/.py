def butterfly_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('*', end='')
        spaces = 2 * (n - i)
        for j in range(1, spaces + 1):
            print(' ', end='')
        for j in range(1, i + 1):
            print('*', end='')
        print()

    for i in range(n, 0, -1):
        for j in range(1, i):
            print('*', end='')
        spaces = 2 * (n - i)
        for j in range(1, spaces + 2):
            print(' ', end='')
        for j in range(1, i):
            print('*', end='')
        print()

# Set the number of rows in the pattern
rows = 4

# Call the function to print the butterfly pattern
butterfly_pattern(rows)
