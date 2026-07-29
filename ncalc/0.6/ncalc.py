# ncalc 0.6
# yep a rename, of course!!!!!

# changelog (incase you dont see the thing)
# - now using numpy instead of math, sorry python 1 users!!
# - WAY, and i mean WAYYY more functions!!! (yes even sine!!)
# - \x1b instead of \033
# - is your terminal good? i hope it supports 24 bit rgb!

# import them damn libraries and doing some shi for extra compatibility
import numpy as np
from colorama import just_fix_windows_console
import time

just_fix_windows_console()

# intro (this code is ASS im CRINE)
while True:
    print("NCalc Menu")
    print("\x1b[1;38;2;54;0;0;48;2;255;85;64m 1. Add \x1b[0m")
    print("\x1b[1;38;2;73;13;0;48;2;255;86;38m 2. Float Add \x1b[0m")
    print("\x1b[1;38;2;97;48;0;48;2;255;136;0m 3. Subtract \x1b[0m")
    print("\x1b[1;38;2;111;87;0;48;2;255;204;0m 4. Float Subtract \x1b[0m")
    print("\x1b[1;38;2;104;104;0;48;2;234;234;0m 5. Multiply \x1b[0m")
    print("\x1b[1;38;2;85;109;0;48;2;195;244;0m 6. Float Multiply \x1b[0m")
    print("\x1b[1;38;2;58;114;0;48;2;136;254;0m 7. Divide \x1b[0m")
    print("\x1b[1;38;2;26;113;0;48;2;68;255;0m 8. Int Divide \x1b[0m")
    print("\x1b[1;38;2;2;113;0;48;2;0;255;0m 9. Exponents \x1b[0m")
    print("\x1b[1;38;2;0;113;24;48;2;0;255;68m 10. Square Root \x1b[0m")
    print("\x1b[1;38;2;0;113;57;48;2;0;255;136m 11. Cube Root \x1b[0m")
    print("\x1b[1;38;2;0;114;90;48;2;0;255;204m 12. Custom Root \x1b[0m")
    print("\x1b[1;38;2;0;112;112;48;2;0;251;251m 13. Sine (NEW!) \x1b[0m")
    print("\x1b[1;38;2;0;83;105;48;2;0;204;255m 14. Cosine (NEW!) \x1b[0m")
    print("\x1b[1;38;2;0;33;71;48;2;52;145;255m 15. Tangent (NEW!) \x1b[0m")
    print('\x1b[1;38;2;210;215;255;48;2;0;68;255m 16. Pi \x1b[0m')
    print("\x1b[1;38;2;179;183;255;48;2;0;0;255m 17. Tau \x1b[0m")
    print("\x1b[1;38;2;197;191;255;48;2;68;0;255m 18. Euler Number \x1b[0m")
    print("\x1b[1;38;2;255;217;255;48;2;136;0;255m 19. Phi (NEW!) \x1b[0m")
    print("\x1b[1;38;2;34;0;45;48;2;217;83;255m 20. NaN \x1b[0m")
    print("\x1b[1;38;2;81;0;81;48;2;255;0;255m 21. Infinity \x1b[0m")
    print("\x1b[1;38;2;74;0;57;48;2;255;52;205m 22. About ncalc \x1b[0m")
    print("\x1b[1;38;2;64;0;29;48;2;255;73;148m 23. Exit \x1b[0m \n")
    
    # function definitions
    def inputs():
        n1 = int(input("\x1b[1;38;2;54;0;0;48;2;255;85;64m First number? \x1b[0m "))
        n2 = int(input("\x1b[1;38;2;2;113;0;48;2;0;255;0m Second number? \x1b[0m "))
        return n1, n2
    
    def float_inputs():
        n1 = float(input("\x1b[1;38;2;54;0;0;48;2;255;85;64m First number? \x1b[0m "))
        n2 = float(input("\x1b[1;38;2;2;113;0;48;2;0;255;0m Second number? \x1b[0m "))
        return n1, n2
    
    def one_input():
        n1 = int(input("\x1b[1;38;2;54;0;0;48;2;255;85;64m Number? \x1b[0m "))
        return n1
    
    def one_float_input():
        n1 = float(input("\x1b[1;38;2;54;0;0;48;2;255;85;64m Number? \x1b[0m "))
        return n1

    # the main code, good luck.
    try:
        us = int(input("\x1b[48;5;231;38;5;16m Select an option\x1b[0m: "))
        
        if us == int(1):
            try:
                a, b = inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m+", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;231;231;0m{int(a) + int(b)}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        elif us == int(2):
            try:
                a, b = float_inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m+", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                holdon = np.round(float(a) + float(b), 5)
                print(f"\x1b[38;2;231;231;0m{holdon}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be float!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(3):
            try:
                a, b = inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m-", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;231;231;0m{int(a) - int(b)}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        elif us == int(4):
            try:
                a, b = float_inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m-", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                holdon = np.round(float(a) - float(b), 5)
                print(f"\x1b[38;2;231;231;0m{holdon}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be float!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(5):
            try:
                a, b = inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255mx", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;231;231;0m{int(a) * int(b)}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(6):
            try:
                a, b = float_inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255mx", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                holdon = np.round(float(a) * float(b), 5)
                print(f"\x1b[38;2;231;231;0m{holdon}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be float!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(7):
            try:
                a, b = float_inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                holdon = np.round(float(a) / float(b), 5)
                print(f"\x1b[38;2;231;231;0m{holdon}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be float!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(8):
            try:
                a, b = inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m//", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;231;231;0m{int(a) // int(b)}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(9):
            try:
                a, b = inputs()
                print(f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m^", f"\x1b[38;2;0;255;0m{b}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;231;231;0m{int(a) ** int(b)}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(10):
            try:
                a = one_input()
                print("\x1b[38;2;255;255;255m√" ,f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;255;128;128m{np.sqrt(int(a))}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(11):
            try:
                a = one_input()
                print("\x1b[38;2;255;255;255m∛the i" ,f"\x1b[38;2;255;85;64m{a}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;255;128;128m{np.cbrt(int(a))}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(12):
            try:
                a, b = inputs()
                print(f"\x1b[38;2;255;85;64m{b}", "\x1b[38;2;255;255;255mˣ√", f"\x1b[38;2;0;255;0m{a}", "\x1b[38;2;255;255;255m=\x1b[0m")
                print(f"\x1b[38;2;231;231;0m{int(a) ** (1/(int(b)))}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't root by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(13):
            try:
                a = one_float_input()
                print(f"\x1b[38;2;255;255;255m{np.sin(float(a))}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(14):
            try:
                a = one_float_input()
                print(f"\x1b[38;2;255;255;255m{np.cos(float(a))}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(15):
            try:
                a = one_float_input()
                print(f"\x1b[38;2;255;255;255m{np.tan(float(a))}\x1b[0m")
            except ValueError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Value must be integer!")
            except ZeroDivisionError:
                print("\x1b[1;38;2;54;0;0;48;2;255;85;64mERROR: Can't divide by 0!")
            
            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(16):
            print(f'\x1b[38;2;255;255;255m{np.pi}')

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(17):
            print(f'\x1b[38;2;255;255;255m{np.pi*2}')

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(18):
            print(f'\x1b[38;2;255;255;255m{np.e}')

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(19):
            print(f'\x1b[38;2;255;255;255m{(1+np.sqrt(5))/2}')

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(20):
            print(f'\x1b[38;2;255;255;255m{np.nan}')

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(21):
            print(f'\x1b[38;2;255;255;255m{np.inf}')

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(22):
            print("\x1b[1;4;5;38;2;0;128;255mncalc 0.6 beta")
            print("\x1b[22;24;25;38;2;255;255;255mThis is a Python passion project, specifically")
            print("\x1b[22;38;2;255;255;255ma calculator that does calculator things. \x1b[2m(wow shocking)")
            print("\x1b[22;38;2;255;255;255mThis IS a beta, so if you experience any bugs, contact me on")
            print("\x1b[1;5;38;2;220;230;255mGithub: sdn2k")
            print("\x1b[1;5;38;2;95;95;255mDiscord: serial.designation.n.2k \x1b[0m")

            us2 = input("\x1b[48;2;0;0;0;38;2;255;255;255m Return to menu? [Y/N]: \x1b[0m")

            if us2 == "y" or us2 == "Y":
                print("Returning to menu...")
                time.sleep(0.25)
                continue
            else: 
                print("Exiting.")
                time.sleep(0.25)
                break

        if us == int(23):
            print("Exiting.")
            break

        else:
            print("\x1b[1;38;2;54;0;0;48;2;255;85;64m Operation not found, returning to menu \x1b[0m")
            time.sleep(0.5)
            continue
        
    except ValueError:
        print("\x1b[1;38;2;54;0;0;48;2;255;85;64m Operation not found, returning to menu \x1b[0m")
        time.sleep(0.5)
        continue