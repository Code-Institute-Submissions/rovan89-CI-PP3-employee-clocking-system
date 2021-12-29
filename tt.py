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
            employee_details = l , n
            return employee_details
        else:
            continue

employee_number = employee_input()
print(">>>", itterate_through_employee_details(employee_number))


