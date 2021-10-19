# 6. Write a Python program to make a dict from these two lists.
# lst1: ['hello', 'bye-bye', 'moon', 'sun', 'star'], lst2: ['բարև', 'հաջող', 'լուսին', 'արև', 'աստղ']

lst1 = ['hello', 'bye-bye', 'moon', 'sun', 'star']
lst2 = ['բարև', 'հաջող', 'լուսին', 'արև', 'աստղ']

_dict = {}
for l1,l2 in zip(lst1,lst2):
    _dict[l1] = l2

print(_dict)