# Programmed by: Mubashir Ahmed OR known as Mubashir78 on Github
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
        sleep(0.03)
    print(" ")


def choices_for_user():
    print_slow(color.BOLD+"Choose the type of operation you wish to apply:"+color.END)
    sleep(0.7)

    print(color.ITALIC+"\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Square of 'x'\n6- Square root of 'x'"+color.END)
    sleep(2)

    choice_of_user()

def choice_of_user():
    print(" ")
    choice = input(color.CYAN+color.BOLD+"Your Choice: "+color.END)
    try:
        choice = int(choice)
    except:
        choice = choice
    finally:
        if choice == 1:
            print(" ")
            print_slow(color.BOLD+color.ITALIC+"|Addition|\n"+color.END)
            sleep(1)

            result = addition()
            sleep(0.7)

            print(" ")
            print(color.GREEN+color.UNDERLINE+f"The result is {result}"+color.END)
            restart_code()

        elif choice == 2:
            print(" ")
            print_slow(color.BOLD+color.ITALIC+"|Subtraction|\n"+color.END)
            sleep(1)
            
            result = subtraction()
            print(" ")
            print(color.GREEN+color.UNDERLINE+f"The result is {result}"+color.END)
            restart_code()

        elif choice == 3:
            print(" ")
            print_slow(color.BOLD+color.ITALIC+"|Multiplication|\n"+color.END)
            sleep(1)
            
            result = multiplication()
            print(" ")
            print(color.GREEN+color.UNDERLINE+f"The result is {result}"+color.END)
            restart_code()

        elif choice == 4:
            print(" ")
            print_slow(color.BOLD+color.ITALIC+"|Division|\n"+color.END)
            sleep(1)
            
            result = division()
            print(" ")
            print(color.GREEN+color.UNDERLINE+f"The result is {result}"+color.END)
            restart_code()

        elif choice == 5:
            print(" ")
            print_slow(color.BOLD+color.ITALIC+"|Square of 'x'|\n"+color.END)
            sleep(1)
            
            result = square_of_x()
            print(" ")
            print(color.GREEN+color.UNDERLINE+f"The result is {result}"+color.END)
            restart_code()

        elif choice == 6:
            print(" ")
            print_slow(color.BOLD+color.ITALIC+"|Square Root of 'x'|\n"+color.END)
            sleep(1)
            
            result = square_root_of_x()
            print(" ")
            print(color.GREEN+color.UNDERLINE+f"The result is {result}"+color.END)
            restart_code()

        else:
            print_slow(error_code)
            sleep(1.3)
            choice_of_user()

def restart_code():
    sleep(0.8)
    
    print(" ")
    restart = input(color.BLUE+color.BOLD+"Do you wish to retry or exit?: "+color.END).lower()
    
    if restart == "retry":
        print(" ")
        choices_for_user()
    
    elif restart == "exit":
        print(" ")
        print_slow(color.BOLD+"The calculator will now exit."+color.END)
        sleep(0.7)
        exit()
    
    else:
        print_slow(error_code)
        print(" ")
        restart_code()

def startup():
    print_slow("===================================")
    print(color.ITALIC+"        'Basic Calculator'")
    print("   Programmed By: Mubashir Ahmed"+color.END)
    print("===================================")
    sleep(2.3)
    choices_for_user()

def input_1():
    a = input(color.CYAN+"Type the first number: "+color.END)
    b = input(color.CYAN+"Type the second number: "+color.END)
    
    try:
        a = float(a)
        try:
            b = float(b)
        
        except ValueError:
            print_slow(error_code)
            sleep(0.7)
            print(" ")
            input_1()

    except ValueError:
        print_slow(error_code)
        sleep(0.7)
        print(" ")
        input_1()

    finally:
        print(" ")
        print_slow(calcul)
        sleep(1)
        return a,b
    
def input_2():
    x = input(color.CYAN+"Type the number: "+color.END)
    
    try:
        x = float(x)

    except ValueError:
        print_slow(error_code)
        sleep(0.7)
        print(" ")
        input_2()
    
    finally:
        print(" ")
        print_slow(calcul)
        sleep(1)
        return x

def addition():
    num1,num2 = input_1()
    result = num1 + num2
    return result

def subtraction():
    num1,num2 = input_1()
    result = num1 - num2
    return result

def multiplication():
    num1,num2 = input_1()
    result = num1 * num2
    return result

def division():
    num1,num2 = input_1()
    result = num1 / num2
    return result

def square_of_x():
    num1 = input_2()
    result = num1 * num1
    return result

def square_root_of_x():
    num1 = input_2()
    result = math.sqrt(num1)
    reduced_result = round(result,3)
    return reduced_result

startup()
# Programmed by: Mubashir Ahmed OR known as Mubashir78 on Github