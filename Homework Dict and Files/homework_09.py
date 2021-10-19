# 9. Write a program that uses a dictionary that contains ten user names and passwords. 
# The program should ask the user to enter their username and password. 

# If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. If
# the username is in the dictionary, but the user does not enter the right password, 
# the program should say that the password is invalid. 

# If the password is correct, then the program should tell the user 
# that they are now logged in to the system.

users = [
    { "username" : "user1", "password" : "password1" },
    { "username" : "user2", "password" : "password2" },
    { "username" : "user3", "password" : "password3" },
    { "username" : "user4", "password" : "password4" },
    { "username" : "user5", "password" : "password5" },
    { "username" : "user6", "password" : "password6" },
    { "username" : "user7", "password" : "password7" },
    { "username" : "user8", "password" : "password8" },
    { "username" : "user9", "password" : "password9" },
    { "username" : "user10", "password" : "password10" },
]

username = input("Please enter your username: ")
    
for user in users:
    if user['username'] == username:
        password = input("Please enter your password: ")
        if password == user['password']:
            print('You are signed in!')
        else:
            print('Your password is incorrect!')
        break
else:
    print('Wrong username! 😈 Try again!')

        






