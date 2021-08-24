# 5-Write a Python that generate new list from a given list, which will contain only even numbers. 
#     nums: [1, 3, 2, 5, 4, 7, 8]
#     output: [2, 4, 8]


numbers = [1, 3, 2, 5, 4, 7, 8]

# Solution 1 #########################################
# even_numbers_list = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers_list.append(number)

# print(f'Even numbers list : {even_numbers_list}')
######################################################


# Solution 2 #########################################
even_numbers_list = [x for x in numbers if x % 2 == 0]
print(even_numbers_list)
######################################################