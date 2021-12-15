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

def employee_clock_in():
    employee_number = input("Please enter you employee number: ")
    
employee_clock_in()
#def main():

#main()