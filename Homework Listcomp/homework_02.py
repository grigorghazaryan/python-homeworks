# 2-Write a Python program to square the elements of a list 
#     nums: [4, 5, 2, 9]
#     output: [16, 25, 4, 81]

numbers = [4, 5, 2, 9]
result = [x * x for x in numbers]

print(f"Result : {result}")