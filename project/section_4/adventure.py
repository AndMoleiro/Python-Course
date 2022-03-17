available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction ")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break

else:
    print("aren't you glad you got out of there: ")


#  # Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
#  for i in range(0, 100, 7):
#      print(i)
#      if i > 0 and i % 11 == 0:
#          break
#
# for i in range(1, 21):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)

