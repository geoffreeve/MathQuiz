# check for a number or a blank...

for item in range(1, 20):

    response = input("Enter a number or press <enter>")

    if response == "xxx":
        break

    elif response == "":
        print("You chose a blank")

    else:

        try:
            response = int(response)
            print("You chose an integer")

        except ValueError:
            print("oops you did not choose an integer")