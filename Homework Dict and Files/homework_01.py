# 1. Write a Python program to read first n lines of a file.

lines = 3

with open("file.txt") as file:
    for f in file.readlines()[0:lines]:
        print(f.rstrip())