# 2-Write a Python program to square the elements of a list 
#     nums: [4, 5, 2, 9]
#     output: [16, 25, 4, 81]

numbers = [4, 5, 2, 9]
result = []

# Solution 1 #########################################
# i = 0
# while i < len(numbers):
#     result.append(numbers[i] ** 2)
#     i += 1
######################################################

# Solution 2 #########################################
for i in numbers:
    result.append(pow(i, 2))
######################################################

print(f"Result : {result}")