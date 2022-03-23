# print("Please choose your option from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("4:\tHave dinner")
# print("5:\tGo to bed")
# print("0:\tExit")
#
# while True:
#     choice = input()
#
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print(f"You chose {choice}")
#
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")


# alternative version

# choice = "-"
# while choice != "0":
#     if choice in "12345":
#         print(f"You chose {choice}")
#
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
#
#     choice = input()

# yet another version

available_activities = ["Learn Python",
                        "Learn Java",
                        "Go swimming",
                        "Have dinner",
                        "Go to bed",
                        "Exit"
                        ]

valid_choices = []
for i in range(1, len(available_activities) + 1):
    valid_choices.append(str(i))
print(valid_choices)

choice = "-"

chosen_activities = []

while choice != '0':
    if choice in valid_choices:
        print(f"Adding {choice}")
        index = int(choice) - 1
        chosen_activity = available_activities[index]
        chosen_activities.append(chosen_activity)
    else:
        print("What do you want to do today?")
        for number, activity in enumerate(available_activities):
            print(f"{number + 1}:\t{activity}")

    choice = input()

print(chosen_activities)