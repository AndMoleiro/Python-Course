# Write a small program to ask for a name and an age.

name = input("What's your name? ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Very well {0}, welcome to your holiday!".format(name))
else:
    print("I'm sorry {0}, come back in {1} years".format(name, (18 - age)))
