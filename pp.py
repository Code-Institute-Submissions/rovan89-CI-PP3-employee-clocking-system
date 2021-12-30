import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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
#User Options Menu

def options_menu():
    """ 
    Gives user an options menu
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out\n 3. Add new employee to system")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")
    if int(options) == 1:
        transfer_of_data()
    elif int(options) == 2:
        #clock_out()
        pass
    elif int(options) == 3:
        add_new_employee()
    else:
        print("***You can only choose one of the given options, please enter a valid number***")
        options_menu()

def employee_input():
    """
    Takes user input (Employee number)
    """
    while True:

        employee_number = input("Please enter you employee number: ")
        validate_employee_number_count(employee_number)

        if validate_employee_number_count(employee_number):
            print("Employee number is valid!")
            break

    return int(employee_number)

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

#Find matching emplyee name to user entered employee number

def itterates_employee_name():
    """
    Itterates throught employees names.
    """
    all_employees_names = [name["name"] for name in employeeList if "name" in name]
    print("-->",all_employees_names)
    return all_employees_names

def list_of_employees_numbers():
    """
    Itterates throught employees numbers.
    """
    all_employees_numbers = [num["employeeNumber"] for num in employeeList if "employeeNumber" in num]
    print("-->", all_employees_numbers)
    return all_employees_numbers

def itterate_through_employee_details(employee_number):
    for l, n in zip(list_of_employees_numbers(), itterates_employee_name()):
        if employee_number is l:
            employee_details = [l , n]
            print(">>>", employee_details)
            return employee_details
        else:
            continue

# Clock in system
def clock_in_time():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")

    return current_time

#Clock Out
def clock_out():
    #print("Running: ",find_last_employee_entry(employee_input()))
    #clock_out_time = clock_in_time()
    sales_worksheet.update("B2", "Devan")

clock_out()

def find_last_employee_entry(employee_number):
    count = 0
    print("Entered Employee Number: ", employee_number)
    new_data_set = data[1:]
    print("This is the new data set: ", new_data_set)
    for i in new_data_set:
        print(">>>", type((int(i[0]))))
        count +=1
        print("This is count ",count)
        if employee_number is int(i[0]):
            print(employee_number, "is >>> to ", i)

            return count
        else:
            print("Faild")
    

#Update Google Sheets

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("in_out_sheet")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def transfer_of_data():
    """
    Takes data in and formats to list.
    Updates csv file
    """
    employee_number = employee_input()
    employee_details = itterate_through_employee_details(employee_number)
    print("employee_details: ", employee_details)
    clockin_time = clock_in_time()
    print(clockin_time)
    csv_result = employee_details + [clockin_time]
    print("CSV: ", csv_result)
    update_sales_worksheet(csv_result)

#Create a New Employee

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

last_employee_in_employeeList = employeeList[-1]["employeeNumber"]
add_one_to_employee_number = int(last_employee_in_employeeList+1)
print("***", int(add_one_to_employee_number))

def add_new_employee():
    entering_name = input("Please enter employee name: ")
    entering_hourly_rate = input("Please enter employee hourly rate: ")
    newEmployeedAdded = newEmployee(add_one_to_employee_number, entering_name, entering_hourly_rate)
    print("This is the new employee number: " , newEmployeedAdded.employeeNumber)
    print("This is the new employee's name: ", newEmployeedAdded.name)
    print("This is the new employee hourly rate: ", newEmployeedAdded.hourlyRate)
    newEmployeedAdded.addingEmployeeDetails()
    print("New employee add successfully: ", employeeList[-1])
    main()

def main():
    options_menu()
    
#main()