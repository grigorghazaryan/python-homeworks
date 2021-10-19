# Write a Python program to combine each line from first file
# with the corresponding line in second file in a dict 
# where keys are the line numbers, 
# and values are the combined lines 
# and print the longest value of that dict.

with open("file.txt") as file1, open("file2.txt") as file2:

    s1 = file1.readline()
    s2 = file2.readline()

    i = 1
    _dict = {}

    while s1 or s2:
        _dict[i] = s1.strip() + " " + s2.strip()

        s1 = file1.readline()
        s2 = file2.readline()

        i += 1

print(_dict)
print(max(_dict, key=lambda s: len(_dict[s])))