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