available_inputs = [0, 1, 2, 3, 4, 5]
chosen_inputs = []

while True:
    input_number = input("Please choose your option from the list below:"
                         "\n1.\tLearn Python"
                         "\n2.\tLearn Java"
                         "\n3.\tGo swimming"
                         "\n4.\tHave dinner"
                         "\n5.\tGo to bed"
                         "\n0.\tExit"
                         "\n")
    if input_number == 0:
        print("Exiting")
        break

    chosen_inputs += input_number
    print("activities chosen: " + str(chosen_inputs))


