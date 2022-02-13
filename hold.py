def find_last_employee_entry(employee_number):
    """
    This function finds the row in Google Sheets of
    number of the employee number that
    was entered by the user
    """
    count = 1
    new_data_set = data[1:]
    for i in new_data_set:
        count += 1
        if employee_number is int(i[0]):

            return count

   for l, n in zip(list_of_employees_numbers(), itterates_employee_name()):
        print("This is Num: ", employee_number)
        print("This is L: ", l)
        print("////////////")
        if employee_number == int(l):
            employee_details = [l, n]
            print(employee_details)
            return employee_details
        else:
            continue 