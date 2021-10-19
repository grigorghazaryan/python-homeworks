# 7․ Write a program that changes the places of the keys and values of a dictionary.
    
_dict = { "Armenia": "Yerevan", "Italy": "Rome", "Japan": "Tokyo" }

output = dict(zip(_dict.values(), _dict.keys()))

print(output)
