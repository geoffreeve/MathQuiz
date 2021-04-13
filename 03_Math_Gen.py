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
    user_answer = int(input("{} {} {} = ".format(num_A, symbol_list[symbol], num_B))

    # Checks if users answer matches programs answer, if it does then it prints correct.
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect")


# Main routine
try:
    # Asks user for 
    symbol = int(input("1.+ 2.- 3.* 4./  "))
    min_num = int(input("Enter minimum number: "))
    max_num = int(input("Enter maximum number: "))
    generate(select, min_num, max_num)

except ValueError:
    raise