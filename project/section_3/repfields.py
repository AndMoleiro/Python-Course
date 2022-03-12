age = 24
# using str() to coerce int to change to str -> can now use concatenate
print("My age is " + str(age) + " years")

# the replacement field is replaced by {0}, which is then replaced by the first value in format()
print("My age is {0} years".format(age))

# the replacement fields are replaced by the values in format
# the first value replaces {0} and so on
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print()

# using triple quotes, we don't need commas
print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
""".format(28, 30, 31))