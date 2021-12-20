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
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"3 values are required, you provided {len(values)}"
            )
        return False

    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n ")
        return False
    
    return True
"""
def validate_employee_number(values):

    try:
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] != int(values):
                print("This is not = ", list_of_numbers[i])
                raise ValueError(
                f"***This is an incorrect employee number, you provided {values}"
                )
            return True

    except ValueError as e: 
            print(f"Invalid entry: {e}, please try again\n ")
            return True
    
    return False
"""

#for i in list_of_numbers:
 #       if values != [i]:
  #          raise ValueError(
   #             f"This is an incorrect employee number"
    #           )
     #   print([i])

def test(values):
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] != int(values):
            print("test This is = ", list_of_numbers[i])
            return True
        else:
            return False

def employee_clock_in():
    """
    #############
    """
    while True:
        print("***Step 1: Input")
        employee_number = input("Please enter you employee number: ")
        print("***Step 1: Input accepted")
        print("***Step 2: Checking amount of numbers entered")
        validate_employee_number_count(employee_number)
        print("***Step 2: amount check completed")
        print("***Step 3: Test current employee number check starting")
        test(employee_number)
        print("***Step 3: Test current employee number check completed")
        #print("***Step 4: OLD current employee number check starting")
        #validate_employee_number(employee_number)
        #print("***Step 4: OLD current employee number check completed***")

        if validate_employee_number_count(employee_number) and validate_employee_number(employee_number):
            print("Valid entry!")
            break

# Add new employee

class newEmployee:
    """
    This class allows the user to enter the necessary values to create a new instance of an employee
    and add it to the employeeList list. 
    """
 


#employee_number = input("Please enter you employee number: ")
#validate_employee_number(employee_number)



def main():
    list_of_employees_numbers()
    print(list_of_numbers) 
    #options_menu()
    employee_clock_in()
    print(list_of_numbers) 

main()