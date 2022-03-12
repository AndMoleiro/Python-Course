#         012345678901234
#         -14 : -1
parrot = "Norwegian Blue"

# print(parrot)
#
# # print we win (one character per line)
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
#
# print()
# # negative indexing in strings
#
# print(parrot[-1])
# print(parrot[-14])
#
# print()
#
# # print we win with negative indexing(one character per line)
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# slicing

# # start at position 0 until, not including, position 6
# print(parrot[0:6])  # Norweg
# print(parrot[3:5])  # we
# print(parrot[0:9])  # Norwegian
# print(parrot[10:])  # Blue

# slicing with step

print(parrot[0:6:2])    # first slice from 0:6 (Norwegi), then second slice on :2 (Nre)
print(parrot[0:6:3])    # first slice from 0:6 (Norwegi), then second slice on :3 (Nw)
