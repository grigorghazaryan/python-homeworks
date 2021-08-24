# 1-Write a Python program to triple all numbers of a given list of integers.
#     nums: [1, 3, 2, 6, 5, 7]
#     output: [3, 9, 6, 18, 15, 21]

numbers = [1, 3, 2, 6, 5, 7]
result = []

# Solution 1 #########################################
# i = 0
# while i < len(numbers):
#     result.append(numbers[i] * 3)
#     i += 1
######################################################

# Solution 2 #########################################
for i in numbers:
    result.append(i * 3)
######################################################

print(f'Result :, {result}')