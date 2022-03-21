# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# # rebinds result to a new value
# result = False
# print(id(result))

result = "correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))