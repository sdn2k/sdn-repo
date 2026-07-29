# libraries
from colorama import just_fix_windows_console
import math
import time

# just making sure
just_fix_windows_console()

# intro
print("\033[38;5;194;48;5;22mWelcome! \033[0m\n\033[38;5;195;48;5;23mThis is the biggest Python project I've ever done, if you")
print("encounter bugs in TFBCalc, notify me on Discord.\033[0m")

# definitions
def menu():
    print("\033[38;5;232;48;5;255m TFBCalc Menu \033[0m")
    print("\033[38;5;217;48;5;52m 1. Addition            2. Float Addition   3. Subtraction          \033[0m")
    print("\033[38;5;229;48;5;58m 4. Float Subtraction   5. Multiplication   6. Float Multiplication \033[0m")
    print("\033[38;5;157;48;5;22m 7. Division            8. Integer Division 9. Exponents            \033[0m")
    print("\033[38;5;159;48;5;23m 10. Square Root        11. Cube Root       12. Custom Roots        \033[0m")
    print("\033[38;5;147;48;5;17m 13. Pi                 14. e               15. Tau                 \033[0m")
    print("\033[38;5;219;48;5;53m 16. About TFBCalc      17. Exit                                    \033[0m")

def error_dividezero():
    print("\033[38;5;216;48;5;52mERROR: Dvision by zero isn't possible\033[0m")

def error_overflow():
    print("\033[38;5;216;48;5;52mERROR: You went past the overflow limit!!\033[0m")

def error_nan():
    print("\033[38;5;216;48;5;52mERROR: Not a number\033[0m")

def notfound():
    print("\033[38;5;225;48;5;53mOperation not found, make sure:")
    print("\033[38;5;225;48;5;53m1. It is a valid integer")
    print("\033[38;5;225;48;5;53m2. The function is implemented \033[0m")

# Foreshadowing (noun): an indication for what is to come
superscripts = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹"
}

def superscript_the_thing(n):
    return "".join(superscripts[d] for d in str(n))

# main code
while True: 
    menu()

    try:
        user_input = int(input("\033[48;5;16;38;5;231mEnter your choice:\033[0m "))
    except ValueError:
        error_nan()
        continue

    # addition
    if user_input == 1:
        try:
            n1 = int(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = int(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m+\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 + n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # float addition
    elif user_input == 2:
        try:
            n1 = float(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = float(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m+\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 + n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()

        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # subtraction
    elif user_input == 3:
        try:
            n1 = int(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = int(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m-\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 - n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # float subtraction
    elif user_input == 4:
        try:
            n1 = float(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = float(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m-\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 - n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # multiplication
    elif user_input == 5:
        try:
            n1 = int(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = int(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231mx\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 * n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # float multiplication
    elif user_input == 6:
        try:
            n1 = float(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = float(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231mx\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 * n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # division
    elif user_input == 7:
        try:
            n1 = float(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = float(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m/\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 / n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        except ZeroDivisionError:
            error_dividezero()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # int division
    elif user_input == 8:
        try:
            n1 = int(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = int(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m//\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", n1 // n2, "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        except ZeroDivisionError:
            error_dividezero()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # exponentiation
    elif user_input == 9:
        try:
            n1 = int(input("\033[48;5;52;38;5;224mFirst number?:\033[0m "))
            n2 = int(input("\033[48;5;22;38;5;194mSecond number?:\033[0m "))
            print("\033[38;5;196m", n1, "\033[38;5;231m^\033[38;5;46m", n2, "\033[38;5;231m=")
            print("\033[38;5;226m", math.pow(n1, n2), "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # square root
    elif user_input == 10:
        try:
            n1 = int(input("\033[48;5;17;38;5;189mNumber to square root?:\033[0m "))
            print("\033[38;5;231m√",n1, "\033[38;5;231m=")
            print("\033[38;5;226m", math.sqrt(n1), "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # cube root
    elif user_input == 11:
        try:
            n1 = int(input("\033[48;5;17;38;5;189mNumber to cube root?:\033[0m "))
            print("\033[38;5;231m∛",n1,"\033[38;5;231m=")
            print("\033[38;5;226m", math.cbrt(n1), "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # custom roots
    elif user_input == 12:
        try:
            n1 = int(input("\033[48;5;52;38;5;224mNumber to root?:\033[0m "))
            n2 = int(input("\033[48;5;22;38;5;194mNth root?:\033[0m "))
            print("\033[38;5;231m", superscript_the_thing(n2) + "\033[38;5;231m√\033[38;5;46m", n1, "\033[38;5;231m=")
            print("\033[38;5;226m", math.pow(n1, 1/n2), "\033[38;5;231m")
        except ValueError or NameError:
            error_nan()
        except OverflowError:
            error_overflow()
        except ZeroDivisionError:
            error_dividezero()
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # pi
    elif user_input == 13:
        print("\033[38;5;21mPi =\033[38;5;231m", math.pi, "\033[0m")
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # e
    elif user_input == 14:
        print("\033[38;5;21mEuler's number =\033[38;5;231m", math.e, "\033[0m")
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # tau
    elif user_input == 15:
        print("\033[38;5;21mTau (2 * pi) =\033[38;5;231m", math.tau, "\033[0m")
        
        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue

    # about!!
    elif user_input == 16:
        print("\033[38;5;202mtfbcalc \033[0m")
        print("\033[38;5;231mversion 0.5 beta \033[0m \n")
        print("The biggest \033[38;5;33mPyt\033[38;5;226mhon \033[0mproject I've made so far. \n")
        print("\033[1;5;48;5;224;38;5;196mNOTE: This is a beta, it WILL have bugs of any kind, please report any you experience!! \033[0m")
        print("\033[38;5;69mDiscord: \033[0mtfb2k")
        print("\033[38;5;231mGithub: \033[0mtfb2k")

        print("\033[38;5;231mGo back to menu?")
        theinput = input("\033[48;5;23;38;5;195mY/N?:\033[0m ")
        if theinput == "n" or theinput == "N":
            print("\033[38;5;224mTFBCalc will now exit. \033[0m")
            break
        else:
            print("\033[48;5;23;38;5;195mReturning to menu... \033[0m")
            continue
    # exit
    elif user_input == 17:
        print("\033[38;5;224mTFBCalc will now exit. \033[0m")
        break
    else:
        notfound()