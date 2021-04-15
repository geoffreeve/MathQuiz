import random

class Gen:
    # This function takes the symbol selected, min num and max num to generate a question that suits the users needs.
    # 'mode' variable checks what mode the user selected so when the equation is finished, it will go back to the selected mode function.
    def generate(self, symbol, min, max, mode):
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
        user_answer = check.number_checker("{} {} {} = ".format(num_A, symbol_list[symbol-1], num_B), 0, 100000, "Please enter a valid number.")
        
        # Checks if users answer matches programs answer, if it does then it prints correct.
        if user_answer == answer:
            print("Correct!")
        else:
            print("Incorrect")
        if mode == 1:
            mode.rounds(symbol, min_num, max_num)

                
    # Error prevention function, checks if user input is valid.
    def number_checker(self, question, min, max, error):
        while True:
            try:
                response = (input(question))
                # If the user enters xx, the program will exit.
                if response == "xx":
                    exit()
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


class Mode:
    def mode_check(self, symbol, min_num, max_num, mode):
        # If user selects rounds mode, Ask how many rounds and pass through rounds function.
        if mode == 1:
            amount_of_rounds = check.number_checker("How many rounds? ", 0, 100, "Please enter a valid number.")
            option.rounds(symbol, min_num, max_num, amount_of_rounds)

    def rounds(self, symbol, min_num, max_num, rounds_left):
        rounds_left -= 1
        check.generate(symbol, min_num, max_num, 1)
        if rounds_left < 1:
            print("GameOver")



# Main routine
print("***Enter 'xx' to exit the program at any time.***")

# Object with number checker and generator
check = Gen()
# Object with modes
option = Mode()

# Ask user to select a symbol
symbol = check.number_checker("1.+ 2.- 3.* 4./  ", 1, 4, "Please enter a valid number.")
# Ask user to input min range number
min_num = check.number_checker("Enter minimum number: ", 1, 100000, "Please enter any number higher than 0")
# Ask user to input max range number
max_num = check.number_checker("Enter maximum number: ", min_num, 100000, "Please enter a number higher than {}".format(min_num))
# Asks user what mode they are playing.
print("Choose a mode")
what_mode = check.number_checker("1.Rounds 2.Timer 3.Unlimited", 0, 3, "Please enter a valid number.")

# Checks what mode the user selected..
option.mode_check(symbol, min_num, max_num, what_mode)
