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
    "employeeNumber": "001",
    "name": "John Doe",
    "hourlyRate": "10.00"
    },
    {
    "employeeNumber": "002",
    "name": "Jane Doe",
    "hourlyRate": "11.00"
    }
]

#print(employeeList)
#print(employeeList[0]["employeeNumber"])

def options_menu():
    """ 
    Gets chosen option from employee to clock in or out
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")

def employee_clock_in():
    """
    #############
    """
    employee_number = input("Please enter you employee number: ")
    validate_employee_number(employee_number)

def validate_employee_number(values):
    """
    Rasises ValueError if value is not an int.
    Checks if there is exactly 3 values.
    Checks if this is a valid employee number.
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"3 values are required, you provided {len(values)}"
            )
        else:
            for i in employeeList:
                if values != i["employeeNumber"]:
                    raise ValueError(
                        f"This is an incorrect employee number"
                    )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n ")

def main():
    options_menu()
    employee_clock_in()
main()