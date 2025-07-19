
# Example arrays
array1 = [1, 2, 3]
array2 = [4, 5, 6]

# Add the arrays element-wise without using numpy
result = [a + b for a, b in zip(array1, array2)]

# Add the arrays element-wise (already done above)
# result = array1 + array2

print("Sum of arrays:", result)
