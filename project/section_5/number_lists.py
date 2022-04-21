# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
#
# print()
# print("mississippi".count("s"))

empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]   # copying a list by slicing
more_numbers = numbers.copy()   # copying a list by using the copy() method
print(more_numbers)
print(numbers is more_numbers)  # check if both lists are the same - false
print(numbers == more_numbers)  # check if both lists have the same values - true

