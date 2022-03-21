shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
# the ids are the same

# concatenating the list with "cookies"
shopping_list += ["cookies"]
print(shopping_list)
print(id(another_list))
# the id remains unchanged

a = b = c = d = e = f = another_list
# same as having
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list

print(a)

print("Adding cream")
b.append("cream")

print(c)