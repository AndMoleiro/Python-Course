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


for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)