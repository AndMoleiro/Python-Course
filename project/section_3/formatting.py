# create a loop for the range
for i in range(1, 13):
    # ** exponent operator
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    # adding ':x' to {0} specifies a width of x
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    # adding '<' will left align, '>' will right align and '^' will center align
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))      # general format -> 15 decimals
print("Pi is approximately {0:12f}".format(22 / 7))     # using 'f' (float) -> 6 decimals
print("Pi is approximately {0:12.50f}".format(22 / 7))  # python ignores width and considers only precision
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72}".format(22 / 7))

    