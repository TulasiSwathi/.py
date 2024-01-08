'''def reverse_string(str1):
  result = ""
  for i in range(len(str1)):
    if str1[i].isdigit():
      result += str1[i]
    else:
      result = str1[i] + result
  return result


str1 = "ab12cd34"
print(reverse_string(str1))'''

def reverse_string(str1):
  """Reverses a string, preserving the indices of the numerics.

  Args:
    str1: The string to reverse.

  Returns:
    A reversed string, with the numerics in their original indices.
  """

  # Keep track of the indices of the numerics and non-numerics.
  numeric_indices = []
  non_numeric_indices = []
  for i in range(len(str1)):
    if str1[i].isdigit():
      numeric_indices.append(i)
    else:
      non_numeric_indices.append(i)

  # Reverse the numerics and non-numerics independently.
  reversed_numerics = []
  for i in reversed(numeric_indices):
    reversed_numerics.append(str1[i])

  reversed_non_numerics = []
  for i in reversed(non_numeric_indices):
    reversed_non_numerics.append(str1[i])

  # Combine the reversed numerics and non-numerics into a single string.
  reversed_string = ""
  for i in range(len(str1)):
    if i in numeric_indices:
      reversed_string += reversed_numerics[numeric_indices.index(i)]
    else:
      reversed_string += reversed_non_numerics[non_numeric_indices.index(i)]

  return reversed_string


str1 = "ab12cd34"
print(reverse_string(str1))