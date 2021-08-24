# 4-Write a Python program to convert a given list of strings into list of lists
#     colors: ['Red', 'Green', 'Black', 'Orange']
#     output: [['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

colors = ['Red', 'Green', 'Black', 'Orange']

# Solution 1 #########################################
# result = []
# for color in colors:
#     color_chars_list = []
#     for color_chars in color:
#         color_chars_list.append(color_chars)
#     result.append(color_chars_list)

# print(result)
######################################################

# Solution 2 #########################################
def string_to_chars(string):
    result = map(list, string)
    return list(result)

print(string_to_chars(colors))
######################################################