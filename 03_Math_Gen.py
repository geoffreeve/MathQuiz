import random

# This function takes the symbol selected, min num and max num to generate a question that suits the users needs.
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

# Error prevention function, checks if user input is valid.
def number_checker(question, min, max, error):
    while True:
        try:
            response = int(input(question))
            if response < min or response >= max:
                print(error)
                continue
            else:
                return response
                break
        except ValueError:
            print(error)
            continue
            

# Main routine
# Ask user to select a symbol
symbol = number_checker("1.+ 2.- 3.* 4./  ", 1, 4, "Please enter a number between 1 and 4.")
min_num = number_checker("Enter minimum number: ", 1, 100000, "Please enter any number higher than 0")
max_num = number_checker("Enter maximum number: ", min_num, 100000, "Please enter a number higher than {}".format(min_num))
generate(symbol, min_num, max_num)