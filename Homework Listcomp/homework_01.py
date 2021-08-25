# 1-Write a Python program to triple all numbers of a given list of integers.
#     nums: [1, 3, 2, 6, 5, 7]
#     output: [3, 9, 6, 18, 15, 21]

numbers = [1, 3, 2, 6, 5, 7]
result = [x * 3 for x in numbers]

print(f'Result :, {result}')