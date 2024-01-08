def reverse_except_numbers(input_str):
    numbers = ''.join(filter(str.isdigit, input_str))
    non_numbers = ''.join(filter(lambda x: not x.isdigit(), input_str))
    reversed_non_numbers = non_numbers[::-1]

    result = []
    num_idx = 0

    for char in input_str:
        if char.isnumeric():
            result.append(numbers[num_idx])
            num_idx += 1
        else:
            result.append(reversed_non_numbers[0])
            reversed_non_numbers = reversed_non_numbers[1:]

    return ''.join(result)

# Example usage
input_value = "ez56d"
result = reverse_except_numbers(input_value)
print(result)
