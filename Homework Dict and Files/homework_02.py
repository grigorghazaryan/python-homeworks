# 2. Write a Python program to read a file line by line and store it into a dict 
# where keys are the line numbers and the values are lines.

dictionary = {}

with open("file.txt") as file:
    for idx, f in enumerate(file.readlines(), start=1):
        dictionary[idx] = f.strip()

print(dictionary)
    