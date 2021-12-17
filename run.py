import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('employee_clocking_system')

in_out_sheet = SHEET.worksheet('in_out_sheet')

data = in_out_sheet.get_all_values()

#print(data)

employeeList = [ {
    "employeeNumber": 111,
    "name": "John Doe",
    "hourlyRate": "10.00"
    },
    {
    "employeeNumber": 112,
    "name": "Jane Doe",
    "hourlyRate": "11.00"
    }
]

def options_menu():
    """ 
    Gets chosen option from employee to clock in or out
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")

#Employee validation

list_of_numbers = []
def list_of_employees_numbers():
    """
    Itterates throught employees numbers.
    """
    for num in employeeList:
        list_of_numbers.append(num["employeeNumber"])
    return list_of_numbers

def validate_employee_number_count(values):
    """
    Rasises ValueError if value is not an int.
    Checks if there is exactly 3 values.
    Checks if this is a valid employee number.
    """
    list_of_employees_numbers()
    try:
        if len(values) != 3:
            raise ValueError(
                f"3 values are required, you provided {len(values)}"
            )
        return False

        """
        this part of the function is not working. 
        Try to add functionality to check if the user enerted a correct user number.
        """

    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n ")
        return False
    
    return True

def validate_employee_number(values):
    for i in list_of_numbers:
        if values != [i]:
            raise ValueError(
                f"This is an incorrect employee number"
               )
        return False

#for i in list_of_numbers:
 #       if values != [i]:
  #          raise ValueError(
   #             f"This is an incorrect employee number"
    #           )
     #   print([i])


def employee_clock_in():
    """
    #############
    """
    while True:
        employee_number = input("Please enter you employee number: ")
        validate_employee_number_count(employee_number)
        validate_employee_number(employee_number)

        if validate_employee_number_count(employee_number):
            print("Valid entry!")
            break


#employee_number = input("Please enter you employee number: ")
#validate_employee_number(employee_number)

def main():
    print(list_of_numbers) 
    list_of_employees_numbers()
    options_menu()
    #employee_clock_in()
    print(list_of_numbers) 

main()