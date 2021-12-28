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


def list_of_employees_numbers():
    """
    Itterates throught employees numbers.
    """
    all_employees_numbers = [num["employeeNumber"] for num in employeeList if "employeeNumber" in num]
    return all_employees_numbers





def employee_input():
    """
    Takes user input (Employee number)
    """
    employee_number = input("Please enter you employee number: ")
    return int(employee_number)
        

def find_employee_details():
    for i in all_employees_numbers:
        print("\n This is i: ", i)
        print("This is itype : ", type(i))
        print("This is entered_number_by_employee: ", entered_number_by_employee)
        if entered_number_by_employee is i:
            print(f" {entered_number_by_employee} is = {i} \n")
            break
        else:
            print("is not = \n")

def main():
    print("-->",all_employees_numbers)
    entered_number_by_employee = employee_input()

    find_employee_details()
    

all_employees_numbers = list_of_employees_numbers()
entered_number_by_employee = employee_input()
print("testing all employees numbers: ", all_employees_numbers)
main()