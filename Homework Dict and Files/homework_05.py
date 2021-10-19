# 5. Python uses the # character to mark the beginning of a comment. 
# The comment continues from the # character to the end of the line containing it.
 
# Python does not provide any mechanism for ending a comment before the end of a line.
# In this exercise, you will create a program that removes all of the comments 
# from a Python source file. 

# Check each line in the file to determine if a # character is present.
# If it is then your program should remove all of the characters from the # character 
# to the end of the line 
# (we will ignore the situation where the comment character occurs inside of a string). 
# Save the modified file using a new name. 

# Both the name of the input file and the name of the output file should be read 
# from the user.

import argparse

parser = argparse.ArgumentParser(description="Desc")

parser.add_argument(dest="filename", 
                    help="input file with two matrices", 
                    metavar="FILE",
                    nargs='+')

args = parser.parse_args()

source_f, output_f = args.filename


new_file=open(output_f,"a+")

with open(source_f) as s_file:
    for line in s_file:
        if "#" in line:
            line = line[:line.index("#")]
        new_file.write(line)
    new_file.close()

    
    
    