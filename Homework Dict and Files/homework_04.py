# 4. Write a Python program 
# that takes a text file as input 
# and returns the number of words of a given text file.

with open("file.txt") as file:

    lines = 0
    words = 0
    chars = 0

    for line in file:

        line = line.strip("\n")

        lines += 1
        words += len(line.split())
        chars += len(line.strip())
        
print(f"There are {lines} lines, {words} words and {chars} chars in this text! Thank you. Bye!")
