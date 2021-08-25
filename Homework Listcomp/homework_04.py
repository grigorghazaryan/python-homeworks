# 4-Write a Python program to convert a given list of strings into list of lists
#     colors: ['Red', 'Green', 'Black', 'Orange']
#     output: [['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

colors = ['Red', 'Green', 'Black', 'Orange']
result =[[col for col in row] for row in colors]

print(result)