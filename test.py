
def options_menu():
    """ 
    Gives user an options menu
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out\n 3. Add new employee to system")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")
    print(options)
    if int(options) == 1:
        main()
    elif int(options) == 2:
        clockout()
    elif int(options) == 3:
        adding_new_employee()
    else:
        print("***You can only choose one of the given options, please enter a valid number***")
        options_menu()

def clock_in():
    print("Running Clockin")

def clock_out():
    print("Running Clockout")

def adding_new_employee():
    print("Running adding_new_employee()")

options_menu()