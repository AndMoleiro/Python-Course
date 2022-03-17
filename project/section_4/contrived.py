numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
# else is used to run some code after the loop terminates normally
else:
    print("All those numbers are fine")