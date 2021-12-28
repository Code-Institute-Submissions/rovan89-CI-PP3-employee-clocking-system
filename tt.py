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

    
def employee_input():
    """
    Takes user input (Employee number)
    """
    employee_number = input("Please enter you employee number: ")
    return int(employee_number)

def itterates_employee_name():
    """
    Itterates throught employees names.
    """
    entered_number_by_employee = employee_input()
    all_employees_names = [name["name"] for name in employeeList if "name" in name]
    print(all_employees_names)
    return all_employees_names

def find_employee_name():
    all_employees_names = itterates_employee_name()
    for i in all_employees_names:
        print("This is the name: ", [i])
        return i

print(find_employee_name())


