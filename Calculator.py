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
    while True:
        print_slow(color.BOLD+"\nChoose the type of operation you wish to apply:"+color.END)
        sleep(0.5)

        print(color.ITALIC+"\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Square of 'x'\n6- Square root of 'x'"+color.END)
        sleep(1)

        choice = _prompt_choice()
        if choice == "retry":
            continue

        if choice in ("exit",):
            return exit_code()

        print(color.GREEN+color.UNDERLINE+f"\nThe result is {choice}"+color.END)
        if not _prompt_restart():
            return exit_code()

def _prompt_choice():
    while True:
        print(" ")
        raw = input(color.CYAN+color.BOLD+"Your Choice: "+color.END)
        try:
            choice = int(raw)
        except ValueError:
            print_slow(error_code)
            sleep(0.8)
            continue

        if choice == 1:
            print_slow(color.BOLD+color.ITALIC+"\n|Addition|"+color.END)
            sleep(0.7)
            return addition()
        if choice == 2:
            print_slow(color.BOLD+color.ITALIC+"\n|Subtraction|"+color.END)
            sleep(0.7)
            return subtraction()
        if choice == 3:
            print_slow(color.BOLD+color.ITALIC+"\n|Multiplication|"+color.END)
            sleep(0.7)
            return multiplication()
        if choice == 4:
            print_slow(color.BOLD+color.ITALIC+"\n|Division|"+color.END)
            sleep(0.7)
            return division()
        if choice == 5:
            print_slow(color.BOLD+color.ITALIC+"\n|Square of 'x'|"+color.END)
            sleep(0.7)
            return square_of_x()
        if choice == 6:
            print_slow(color.BOLD+color.ITALIC+"\n|Square Root of 'x'|"+color.END)
            sleep(0.7)
            return square_root_of_x()

        print_slow(error_code)
        sleep(0.8)

def _prompt_restart():
    while True:
        sleep(0.8)
        restart = input(color.BLUE+color.BOLD+"\nDo you wish to retry or exit?: "+color.END).lower()
        if restart == "retry":
            return True
        if restart == "exit":
            print_slow(color.BOLD+"\nThe calculator will now exit."+color.END)
            sleep(0.7)
            return False
        print_slow(error_code)

def exit_code():
    print_slow(color.BOLD+"\nThe calculator will now exit."+color.END)
    sleep(0.7)

def startup():
    print_slow("===================================")
    print(color.ITALIC+"        'Basic Calculator'")
    print("   Programmed By: Mubashir Ahmed"+color.END)
    print("===================================")
    sleep(2)
    choices_for_user()

if __name__ == "__main__":
    startup()

def input_1(sign):
    while True:
        user_input = input("\nEnter the numbers with the appropriate sign in between: ")
        input_list = user_input.split(f"{sign}")
        float_list = []

        for num in input_list:
            try:
                float_list.append(float(num))
            except ValueError:
                print_slow(error_code)
                sleep(0.7)
                break
        else:
            print_slow(f"\n{calcul}")
            sleep(1)
            return float_list

def input_2():
    while True:
        x = input(color.CYAN+"\nType the number: "+color.END)
        try:
            x = float(x)
        except ValueError:
            print_slow(error_code)
            sleep(0.7)
            continue
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
    while True:
        num_list = input_1("/")
        div = num_list[0]
        try:
            for num in num_list[1:]:
                div = div / num
        except ZeroDivisionError:
            print_slow(color.BOLD+color.RED+color.UNDERLINE+"Division by zero is not allowed."+color.END)
            sleep(0.8)
            continue
        return round(div, 5)

def square_of_x():
    num1 = input_2()
    result = num1 ** 2
    return result

def square_root_of_x():
    num1 = input_2()
    result = math.sqrt(num1)
    return round(result, 5) 


