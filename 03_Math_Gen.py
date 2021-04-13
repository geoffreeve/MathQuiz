import random

# Main routine
try:
    selection = int(input("1.+ 2.- 3./ 4.*"))
    i = 0
    while i < 4:
        i+=1
        if selection == i:
            math([i])
        else:
            continue

except ValueError:
    print("Error")
    
def math(select):