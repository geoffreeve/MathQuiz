import random


def generate(symbol, min, max):
    # Generates numbers between the min and max numbers inputted by user
    num_A = random.randint(min, max)
    num_B = random.randint(min, max)

    # This symbol list is used in the question print statement later so that i don't have to
    # Repeat print statements for different symbols
    symbol_list = ["+", "-", "*", "/"]

    # Creates answer for Addition
    if symbol == 1:
        answer = num_A + num_B
    # Creates answer for Subtraction
    if symbol == 2:
        answer = num_A - num_B
    # Creates answer for Multiplication
    if symbol == 3:
        answer = num_A * num_B
    # Creates answer for Division
    if symbol == 4:
        answer = num_A / num_B

    # This print statement takes the first generated number, the symbol from the symbol list, and last generated number.
    user_answer = int(input("{} {} {} = ".format(num_A, symbol_list[symbol-1], num_B)))
    
    # Checks if users answer matches programs answer, if it does then it prints correct.
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect")


# Main routine
while True:
    try:
        # Ask user to select a symbol
        symbol = int(input("1.+ 2.- 3.* 4./  "))
        # If the user enters a number lower than 0 or higher than 4, it will print an error and ask the user to try again
        if symbol <= 0 or symbol >= 5:
            print("Please enter a number between 1-4.")
            continue
        # If the user enters 0 or lower, it prints a error and asks the user to try again
        min_num = int(input("Enter minimum number: "))
        if min_num <= 0:
            print("Please enter a number higher than 0.")
            continue
        # If the user enters a number lower than the minimum number, it will print an error and ask the user to try again.
        max_num = int(input("Enter maximum number: "))
        if max_num >= min_num:
            print("Please enter a number higher than min num. Min num: {}".format(min_num))
            continue
        generate(symbol, min_num, max_num)

    except ValueError:
        print("Please enter a number")