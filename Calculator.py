# Programmed by: Mubashir Ahmed OR known as Mubashir78 on Github
# https://www.github.com/Mubashir78

import math
from time import sleep
from sys import stdout

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

error_code = color.BOLD+color.RED+color.UNDERLINE+"Invalid input. Try again.\n"+color.END
calcul = color.ITALIC+"Calculating..."+color.END

def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.025)
    print(" ")


def choices_for_user():
    print_slow(color.BOLD+"\nChoose the type of operation you wish to apply:"+color.END)
    sleep(0.5)

    print(color.ITALIC+"\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Square of 'x'\n6- Square root of 'x'"+color.END)
    sleep(1)

    return choice_of_user()

def choice_of_user():
    print(" ")
    choice = input(color.CYAN+color.BOLD+"Your Choice: "+color.END)
    try:
        choice = int(choice)

    except ValueError:
        print_slow(error_code)
        sleep(0.8)
        return choice_of_user()

    if choice == 1:
        print_slow(color.BOLD+color.ITALIC+"\n|Addition|"+color.END)
        sleep(0.7)

        result = addition()
        print(color.GREEN+color.UNDERLINE+f"\nThe result is {result}"+color.END)
        return restart_code()

    elif choice == 2:
        print_slow(color.BOLD+color.ITALIC+"\n|Subtraction|"+color.END)
        sleep(0.7)
        
        result = subtraction()
        print(color.GREEN+color.UNDERLINE+f"\nThe result is {result}"+color.END)
        return restart_code()

    elif choice == 3:
        print_slow(color.BOLD+color.ITALIC+"\n|Multiplication|"+color.END)
        sleep(0.7)
        
        result = multiplication()
        print(color.GREEN+color.UNDERLINE+f"\nThe result is {result}"+color.END)
        return restart_code()

    elif choice == 4:
        print_slow(color.BOLD+color.ITALIC+"\n|Division|"+color.END)
        sleep(0.7)
        
        result = division()
        print(color.GREEN+color.UNDERLINE+f"\nThe result is {result}"+color.END)
        return restart_code()

    elif choice == 5:
        print_slow(color.BOLD+color.ITALIC+"\n|Square of 'x'|"+color.END)
        sleep(0.7)
        
        result = square_of_x()
        print(color.GREEN+color.UNDERLINE+f"\nThe result is {result}"+color.END)
        return restart_code()

    elif choice == 6:
        print_slow(color.BOLD+color.ITALIC+"\n|Square Root of 'x'|"+color.END)
        sleep(0.7)
        
        result = square_root_of_x()
        print(color.GREEN+color.UNDERLINE+f"\nThe result is {result}"+color.END)
        return restart_code()


def restart_code():
    sleep(0.8)
    restart = input(color.BLUE+color.BOLD+"\nDo you wish to retry or exit?: "+color.END).lower()
    
    if restart == "retry":
        return choices_for_user()
    
    elif restart == "exit":
        print_slow(color.BOLD+"\nThe calculator will now exit."+color.END)
        return sleep(0.7)
    
    else:
        print_slow(error_code)
        return restart_code()

def startup():
    print_slow("===================================")
    print(color.ITALIC+"        'Basic Calculator'")
    print("   Programmed By: Mubashir Ahmed"+color.END)
    print("===================================")
    sleep(2)
    choices_for_user()

def input_1(sign):
    user_input = input("\nEnter the numbers with the appropriate sign in between: ")
    input_list = user_input.split(f"{sign}")
    float_list = []

    for num in input_list:
        try:
            float_list.append(float(num))

        except ValueError:
            print_slow(error_code)
            sleep(0.7)
            return input_1(sign)

    del input_list
    print_slow(f"\n{calcul}")
    sleep(1)
    return float_list
    
def input_2():
    x = input(color.CYAN+"\nType the number: "+color.END)
    
    try:
        x = float(x)

    except ValueError:
        print_slow(error_code)
        sleep(0.7)
        return input_2()
    
    print_slow(f"\n{calcul}")
    sleep(0.8)
    return x

def addition():
    num_list = input_1("+")
    addition = num_list[0]

    for num in num_list[1:]:
        addition = addition + num
    return addition

def subtraction():
    num_list = input_1("-")
    subtraction = num_list[0]

    for num in num_list[1:]:
        subtraction = subtraction - num
    return subtraction

def multiplication():
    num_list = input_1("*")
    multiplication = num_list[0]
    
    for num in num_list[1:]:
        multiplication = multiplication * num
    
    return multiplication

def division():
    num_list = input_1("/")
    division = num_list[0]

    for num in num_list[1:]:
        division = division / num
    return round(division, 5)

def square_of_x():
    num1 = input_2()
    result = num1 ** 2
    return result

def square_root_of_x():
    num1 = input_2()
    result = math.sqrt(num1)
    return round(result, 5) 

startup()
# Programmed by: Mubashir Ahmed OR known as Mubashir78 on Github
# https://www.github.com/Mubashir78
