import random

highest = 100
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
print(f"Please guess a number between 1 and {highest}: ")
guess = 0   # initialize to any number that doesn't equal the answer

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("game over")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")








