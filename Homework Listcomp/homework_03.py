# 3-Write a Python program to convert a given list of integers and a tuple of integers in a list 
# of strings and print result.
#     nums_l: [1,2,3,4]
#     nums_t: (10, 20, 30, 40)
#     ouput: 
#            List of strings:
#            ['1', '2', '3', '4']
#            Tuple of strings:
#            ('0', '1', '2', '3')

numbers_list = [1,2,3,4]
numbers_tuple = (10, 20, 30, 40)

# For list
# result_list = []
# for i in numbers_list:
#     result_list.append(str(i))

result_list = list(map(str, numbers_list))
result_tuple = tuple(map(str, numbers_tuple))

print(f'List : {result_list}')
print(f'Tuple : {result_tuple}')