# current_choice = "-"
# computer_parts = []     # create an empty list
#
# while current_choice != '0':
#     if current_choice in "123456":
#         print(f"Adding {current_choice}")
#         if current_choice == "1":
#             computer_parts.append("computer")
#         elif current_choice == "2":
#             computer_parts.append("monitor")
#         elif current_choice == "3":
#             computer_parts.append("keyboard")
#         elif current_choice == "4":
#             computer_parts.append("mouse")
#         elif current_choice == "5":
#             computer_parts.append("mouse mat")
#         elif current_choice == "6":
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add options from the list below")
#         print("1:\tcomputer")
#         print("2:\tmonitor")
#         print("3:\tkeyboard")
#         print("4:\tmouse")
#         print("5:\tmouse mat")
#         print("6:\thdmi cable")
#         print("0:\tto finish")
#
#     current_choice = input()
#
# print(computer_parts)

# alternative way

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):    # loop to print the index numbers of the available parts
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []     # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        print(chosen_part)
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}:\t{part}")

        # for part in available_parts:
            # (f"{available_parts.index(part) + 1}: {part}")

    current_choice = input()

print(computer_parts)