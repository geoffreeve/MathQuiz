import random


# This function takes the symbol selected, min num and max num to generate a question that suits the users needs.
def generate(symbol, min, max, rounds):
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
    user_answer = number_checker("{} {} {} = ".format(num_A, symbol_list[symbol-1], num_B), 0, 100000, "Please enter a valid number.")
    
    # Checks if users answer matches programs answer, if it does then it prints correct.
    if user_answer == answer:
        print("Correct!")
        rounds -= 1
        return rounds
    else:
        print("Incorrect")

            
def selection():
    # Ask user to select a symbol
    symbol = number_checker("1.+ 2.- 3.* 4./  ", 1, 4, "Please enter a valid number.")
    # Ask user to input min range number
    min_num = number_checker("Enter minimum number: ", 1, 100000, "Please enter any number higher than 0")
    # Ask user to input max range number
    max_num = number_checker("Enter maximum number: ", min_num, 100000, "Please enter a number higher than {}".format(min_num))

    # Asks user how many rounds they want
    rounds = number_checker("How many rounds: ", 1, 100000, "Please enter a valid integer higher than 0")
    print("Rounds left: {}".format(rounds))
    while rounds > 0:
        print(rounds)
        # Calls generate function to generate a equation with the given values (symbol, min-max number range).
        generate(symbol, min_num, max_num, rounds)
        rounds -= 1
    print("GameOver")


# Error prevention function, checks if user input is valid.
def number_checker(question, min, max, error):
    while True:
        try:
            response = (input(question))
            # If the user enters xx, the program will exit.
            if response == "xx":
                selection()
            # Checks if the user has entered a response that is both higher than min and lower than max.
            elif int(response) < min or int(response) > max:
                print(error)
                continue
            # If the response is valid it will be returned
            else:
                return int(response)
        # If the user enters anything invalid that hasn't been covered by if statements, it will be caught here with a error printed.
        except ValueError:
            print(error)
            continue


# Main routine
# Short instructions
print("***Enter 'xx' to exit the program at any time.***")
selection()