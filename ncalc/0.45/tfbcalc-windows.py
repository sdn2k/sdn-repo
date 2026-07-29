# libraries
import time
import winsound
import math

# logo intro with beep
print("\033[38;5;202m████████ ███████ ██████   ██████  █████  ██       ██████ \033[0m TM")
time.sleep(0.1)
print("\033[38;5;214m   ██    ██      ██   ██ ██      ██   ██ ██      ██      ")
time.sleep(0.1)
print("\033[38;5;202m   ██    █████   ██████  ██      ███████ ██      ██      ")
time.sleep(0.1)
print("\033[38;5;214m   ██    ██      ██   ██ ██      ██   ██ ██      ██      ")
time.sleep(0.1)
print("\033[38;5;202m   ██    ██      ██████   ██████ ██   ██ ███████  ██████ \033[0m")
print("Loading...")
time.sleep(1.0)
print("\033[92mDone! \033[0m \n")
winsound.Beep(1100, 600)

# welcome! intro
print("\033[38;5;34m██     ██ ███████ ██       ██████  ██████  ███    ███ ███████ ██ ")
time.sleep(0.1)
print("\033[38;5;120m██     ██ ██      ██      ██      ██    ██ ████  ████ ██      ██ ")
time.sleep(0.1)
print("\033[38;5;34m██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████   ██ ")
time.sleep(0.1)
print("\033[38;5;120m██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██         ")
time.sleep(0.1)
print("\033[38;5;34m ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ ██\033[0m")
time.sleep(1.0)
print("This is my \033[91mBIGGEST \033[0mproject yet, so if you find any bugs, please report")
time.sleep(0.8)
print("them to me on \033[38:5:63mDiscord. \033[0m \n")

# select!!!!!!!!!!
def selectscreen():
    time.sleep(1.0)
    print("\033[38;5;196m███████ ███████ ██      ███████  ██████ ████████")
    time.sleep(0.1)
    print("\033[38;5;226m██      ██      ██      ██      ██         ██    ")
    time.sleep(0.1)
    print("\033[38;5;46m███████ █████   ██      █████   ██         ██    ")
    time.sleep(0.1)
    print("\033[38;5;51m     ██ ██      ██      ██      ██         ██    ")
    time.sleep(0.1)
    print("\033[38;5;21m███████ ███████ ███████ ███████  ██████    ██    \033[0m")
    time.sleep(1.0)
    print("\033[1;38;5;9m1. Addition \033[38;5;1m")
    print("Adds two integer numbers \n")

    time.sleep(0.3)
    print("\033[1;38;5;11m2. Subtraction \033[38;5;3m")
    print("Subtracts two integer numbers \n")

    time.sleep(0.3)
    print("\033[1;38;5;10m3. Multiplication \033[38;5;2m")
    print("Multiplies two integer numbers \n")

    time.sleep(0.3)
    print("\033[38;5;14m4. Integer Division \033[38;5;6m")
    print("Divides two integer numbers.")
    print("Finds the closest answer that")
    print("is an integer. \n")

    time.sleep(0.3)
    print("\033[38;5;12m5. Factorial \033[38;5;4m")
    print("Multiplies the integer by n - 1")
    print("of itself until reaching 1 \n")

    time.sleep(0.3)
    print('\033[38;5;13m6. Float Addition \033[38;5;5m')
    print("Adds two float numbers \n")

    time.sleep(0.3)
    print("\033[38;5;9m7. Float Subtraction \033[38;5;1m")
    print("Subtracts two float numbers \n")

    time.sleep(0.3)
    print("\033[38;5;11m8. Float Multiplication \033[38;5;3m")
    print("Multiplies two float numbers \n")

    time.sleep(0.3)
    print("\033[38;5;10m9. Float/Regular Division \033[38;5;2m")
    print("Divides two float numbers")

    time.sleep(0.3)
    print("\033[38;5;14m10. About \033[38;5;6m")
    print("About the Python program :D \n")

    time.sleep(0.3)
    print('\033[38;5;12m11. Exit \033[38;5;4m')
    print("Exit the program. \033[0m")

    time.sleep(0.3)
    print("More operations will be added!!")

selectscreen()

# input.
try:
    user = int(input("\033[38;5;231mChoose your option: "))
except ValueError as e:
    def crash_value():
        winsound.Beep(1000, 700)
        print("\033[48;5;52;38;5;9m")
        print("██████     ")
        print("██   ██ ██ ")
        print("██   ██    ")
        print("██   ██ ██ ")
        print("██████      \033[1;48;5;52;38;5;196m \n")
        time.sleep(0.5)
        print("TFBCalc has crashed. \033[0m")
        time.sleep(1.0)
        print("TFBCalc ran into an exception, causing Python to")
        print("bring a status code of \033[91m1\033[0m. \n")

        print("\033[38;5;210mWhat happened?: \033[0m", e)
        exit_input = input("Press any key to exit: ")
        exit()
    
    crash_value()

# addition 
if user == int(1):
    def addition():
        print("\033[38;5;9mAddition! \033[0m")
        time.sleep(0.5)
        try:
            n1 = int(input("\033[91mFirst number?: \033[0m"))
            n2 = int(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "+", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        print("\033[93m", n1 + n2, "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    addition()

# subtraction
elif user == int(2):
    def subtraction():
        print("\033[38;5;11mSubtraction! \033[0m")
        time.sleep(0.5)
        try:
            n1 = int(input("\033[91mFirst number?: \033[0m"))
            n2 = int(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "-", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        print("\033[93m", n1 - n2, "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    subtraction()

# multplication
elif user == int(3):
    def multiplication():
        print("\033[38;5;10mMultiplication! \033[0m")
        time.sleep(0.5)
        try:
            n1 = int(input("\033[91mFirst number?: \033[0m"))
            n2 = int(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "x", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        print("\033[93m", n1 * n2, "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    multiplication()

# i division
elif user == int(4):
    def integer_division():
        print("\033[38;5;14mInteger Division! \033[0m")
        time.sleep(0.5)
        try:
            n1 = int(input("\033[91mFirst number?: \033[0m"))
            n2 = int(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "/", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        try:
            print("\033[93m", n1 // n2, "\033[0m")
        except ZeroDivisionError as e:
            def crash_zero():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m2\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
                
            crash_zero()
        
        exit_input = input("Press any key to exit: ")
        exit()

    integer_division()

# factorial
elif user == int(5):
    def factorial():
        print("\033[38;5;12mFactorial! \033[0m")
        time.sleep(0.5)
        try:
            n1 = int(input("\033[91mNumber to calculate the factorial of?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[97mThe factorial of\033[92m", n1, "\033[97mis \033[0m")

        time.sleep(0.5)
        print("\033[1;94m", math.factorial(n1), "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    factorial()

# f addition
elif user == int(6):
    def float_addition():
        print("\033[38;5;13mFloat Addition! \033[0m")
        time.sleep(0.5)
        try:
            n1 = float(input("\033[91mFirst number?: \033[0m"))
            n2 = float(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "+", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        print("\033[93m", n1 + n2, "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    float_addition()

elif user == int(7):
    def float_subtraction():
        print("\033[38;5;9mFloat Subtraction! \033[0m")
        time.sleep(0.5)
        try:
            n1 = float(input("\033[91mFirst number?: \033[0m"))
            n2 = float(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "-", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        print("\033[93m", n1 - n2, "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    float_subtraction()

# f multiplication
elif user == int(8):
    def float_multiplication():
        print("\033[38;5;11mMultiplication! \033[0m")
        time.sleep(0.5)
        try:
            n1 = float(input("\033[91mFirst number?: \033[0m"))
            n2 = float(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "x", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        print("\033[93m", n1 * n2, "\033[0m")
        exit_input = input("Press any key to exit: ")
        exit()

    float_multiplication()

# division
elif user == int(9):
    def division():
        print("\033[38;5;14mDivision! \033[0m")
        time.sleep(0.5)
        try:
            n1 = float(input("\033[91mFirst number?: \033[0m"))
            n2 = float(input("\033[92mSecond number?: \033[0m"))
        except ValueError as e: 
            def crash_value():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m1\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
    
            crash_value()

        time.sleep(0.5)
        print("\033[91m", n1, "\033[97m", "/", "\033[92m", n2, "\033[97m", "=")

        time.sleep(0.5)
        try:
            print("\033[93m", n1 / n2, "\033[0m")
        except ZeroDivisionError as e:
            def crash_zero():
                winsound.Beep(1000, 700)
                print("\033[48;5;52;38;5;9m")
                print("██████     ")
                print("██   ██ ██ ")
                print("██   ██    ")
                print("██   ██ ██ ")
                print("██████      \033[1;48;5;52;38;5;196m \n")
                time.sleep(0.5)
                print("TFBCalc has crashed. \033[0m")
                time.sleep(1.0)
                print("TFBCalc ran into an exception, causing Python to")
                print("bring a status code of \033[91m2\033[0m. \n")

                print("\033[38;5;210mWhat happened?: \033[0m", e)
                exit_input = input("Press any key to exit: ")
                exit()
                
            crash_zero()
        
        exit_input = input("Press any key to exit: ")
        exit()

    division()

elif user == int(10):
    def about():
        print("\033[38;5;202m████████ ███████ ██████   ██████  █████  ██       ██████ \033[0m TM")
        time.sleep(0.1)
        print("\033[38;5;214m   ██    ██      ██   ██ ██      ██   ██ ██      ██      ")
        time.sleep(0.1)
        print("\033[38;5;202m   ██    █████   ██████  ██      ███████ ██      ██      ")
        time.sleep(0.1)
        print("\033[38;5;214m   ██    ██      ██   ██ ██      ██   ██ ██      ██      ")
        time.sleep(0.1)
        print("\033[38;5;202m   ██    ██      ██████   ██████ ██   ██ ███████  ██████ \033[0m")

        time.sleep(0.5)
        print("\033[97mVersion 0.45 alpha build \033[0m")
        print("\033[38;5;63mDiscord: \033[0mtfb2k")
        print("\033[38;5;9mIf you find any bugs, report them to my Discord \033[0m \n")

        print("\033[1;4;38;5;231mStatus Codes:\033[0m")
        print("\033[92m0: yippee :3")
        print("\033[1;91m1: valueerror")
        print("\033[1;91m2: zerodivisionerror \033[0m \n")
        time.sleep(2.0)
        exit_input = input("Press any key to exit: ")
        exit()

    about()

elif user == int(11):
    exit_input = input("Press any key to exit: ")
    exit()

else:
    print("\033[48;5;53;38;5;213m")
    print("██   ██  ██████  ██   ██ ")
    print("██   ██ ██  ████ ██   ██ ")
    print("███████ ██ ██ ██ ███████ ")
    print("     ██ ████  ██      ██ ")
    print("     ██  ██████       ██ \033[1;48;5;53;38;5;201m \n")
    print("Not found.")
    print("- Try entering the numbers that are on the list")
    print("- Or the operation isn't available, contact me on Discord if so. \033[0m")
    exit_input = input("Press any key to exit: ")
    exit()