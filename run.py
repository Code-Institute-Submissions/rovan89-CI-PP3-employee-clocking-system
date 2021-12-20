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

def clock_out():
    print("Running Clockout")

def adding_new_employee():
    print("Running adding_new_employee()")

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

    def __init__(self, employeeNumber, name, hourlyRate):
        self.employeeNumber = employeeNumber
        self.name = name
        self.hourlyRate = hourlyRate
 
    def addingEmployeeDetails(self):
        employee = {
            "employeeNumber": int(f"{self.employeeNumber}"),
            "name": f"{self.name}",
            "hourlyRate": f"{self.hourlyRate}"
            }
        employeeList.append(employee)

def adding_new_employee():
    last_employee_in_employeeList = employeeList[-1]["employeeNumber"]
    add_one_to_employee_number = int(last_employee_in_employeeList +1 )
    print("***", add_one_to_employee_number)

    entering_name = input("Please enter employee name: ")
    entering_hourly_rate = input("Please enter employee hourly rate: ")
    newEmployeedAdded = newEmployee(add_one_to_employee_number, entering_name, entering_hourly_rate)
    print("This is the new employee number: " , newEmployeedAdded.employeeNumber)
    print("This is the new employee's name: ", newEmployeedAdded.name)
    print("This is the new employee hourly rate: ", newEmployeedAdded.hourlyRate)
    return newEmployeedAdded.addingEmployeeDetails()
    print("You have added a new employee to the database >>>", employeeList)


#employee_number = input("Please enter you employee number: ")
#validate_employee_number(employee_number)



def clock_in():
    list_of_employees_numbers()
    print(list_of_numbers) 
    #options_menu()
    employee_clock_in()
    print(list_of_numbers) 

options_menu()