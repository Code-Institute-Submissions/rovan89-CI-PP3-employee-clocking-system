
def options_menu():
    """ 
    Gives user an options menu
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out\n 3. Add new employee to system")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")
    print(options)
    if int(options) == 1:
        clock_in()
    elif int(options) == 2:
        clock_out()
    elif int(options) == 3:
        adding_new_employee()
    else:
        print("***You can only choose one of the given options, please enter a valid number***")
        options_menu()

def clock_in():
    print("Running Clock in function")
    employee_input()

def clock_out():
    print("Running Clockout")

def adding_new_employee():
    print("Running adding_new_employee()")

def employee_input():
    """
    This function takes in the employee number
    """
    while True:

        employee_number = input("Please enter you employee number: ")
        validate_employee_number_count(employee_number)

        if validate_employee_number_count(employee_number):
            print("Employee number is valid!")
            break

    return employee_number

def validate_employee_number_count(values):
    """
    Rasises ValueError if value is not an int.
    Checks if there is exactly 3 values.
    """
    print(values)
    try: 
        if len(values) != 3:
            raise ValueError(
                f"3 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n ")
        return False

    return True

    


employee_input()
#options_menu()