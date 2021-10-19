# 8. Your program should read a message from the user. 
# Then it should translate all of the letters and digits in the message to Morse code, 
# leaving a space between each sequence of dashes and dots. 

# Your program should ignore any characters that are not
# listed in the previous table. 
# The Morse code for Hello, World! is shown below:
#  .... . .-.. .-.. --- .-- --- .-. .-.. -..

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-',     'B':'-...',
                    'C':'-.-.',   'D':'-..',   'E':'.',
                    'F':'..-.',   'G':'--.',   'H':'....',
                    'I':'..',     'J':'.---',  'K':'-.-',
                    'L':'.-..',   'M':'--',    'N':'-.',
                    'O':'---',    'P':'.--.',  'Q':'--.-',
                    'R':'.-.',    'S':'...',   'T':'-',
                    'U':'..-',    'V':'...-',  'W':'.--',
                    'X':'-..-',   'Y':'-.--',  'Z':'--..',
                    '1':'.----',  '2':'..---', '3':'...--',
                    '4':'....-',  '5':'.....', '6':'-....',
                    '7':'--...',  '8':'---..', '9':'----.',
                    '0':'-----',  ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

input_text = input("Please enter your text: ")
output_text = ""

for ch in input_text:
    output_text += MORSE_CODE_DICT[ch.upper()]

print(output_text)