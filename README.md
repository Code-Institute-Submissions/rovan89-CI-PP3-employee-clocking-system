# Employee Clock in System
(Developer: Devan Hayes)
[Employee Clocking System Live](https://employee-clocking-system.herokuapp.com/)

![Deployed Program](assets/images/readme_images/deployed_program.PNG)
![Google Sheets Image](assets/images/readme_images/employee_clocking_system.PNG)


## Tables of Contents
1. [Project Goals](#project-goals)
    1. [User Experience](#user-experience)
    2. [Target Audience](#target-audience)
    3. [User Stories](#user-stories)
    4. [Business Owner Stories](#business-owner-stories)
2. [Features](#features)
    1. [Options Menu](#options-menu)
    2. [Clock In](#clock-in)
    3. [Clock Out](#clock-out)
    4. [User Feedback](#user-feedback)
    5. [Exit](#exit)
3. [User Input Validation](#user-input-validation)
4. [Languages](#languages)
5. [Frameworks and Tools](#frameworks-and-tools)
6. [Bugs](#bugs)
7. [Testing](#testing)
8. [Validator Testing](#validator-testing)
9. [Deployment](#deployment)
10. [Credits](#credits)

## Project Goals
Employee Clock In System is a program that allows employees of a business to clock in and out. This facilitates the owners with the necessary data they need to track the employees' hours.

### User Experience
The user first decides which option they would like to do, then a google sheet is updated with the data. 

### Target Audience
- Bussiness' that would like to track employee clock in and out times

### User Stories
1. As a user, I want to log the exact time of arrival.
2. As a user, I want to log the exact leaving time.

### Business Owner Stories
1. As a busisness owner, I want to track all of my employees working hours.
2. As a busisness owner, I want to be able to add new employees to the program.

## Features
### Options Menu
- The options menu has four options to choose from.
    - Option one allows the user to clock in by entering their employee number.
    - Option two allows the user to clock out.
    - Option three allows the user to add new employees to the list of current employees
    - Option four allows the user to quit running the program.

![Options Menu Image](assets/images/readme_images/landing_menu.PNG)

### Clock In (Option One)
- The clock-in option allows an existing employee to enter their employee number.
- The nubmer runs through a validation function to check the correct lenght of the number entered.
- This then creates a new row in the Google Sheet (employee_clocking_system) and inputs the employees number, name and time of clock in.

![Clockin system and results](assets/images/readme_images/clocking_in_system.PNG)

### Clock Out (Option Two)
-The clock-out option allows a user who has already clocked in to add a clock-out time to the row created in the clock-in section (Google Sheets)

![Clocking out](assets/images/readme_images/clocking_out.PNG)

### Create New Employee (Option Three)
- This option allows the user to add a new employee to the list.
    - First the user is prompted to enter a user name.
    - Next the user is prompted to add the hourly rate of the new employee.
    - Finally the new user is assigned an employee number and a new employee has been successfully added to the list

![Adding new employee](assets/images/readme_images/adding_new_employee.PNG)

### User Feedback (Option Four)
- The User Feedback option allows the user to give feedback.
- The user enters their feedback and the user_feedback worksheet in google sheets is updated

![User Feedback](assets/images/readme_images/user_feedback.PNG)

### Exit (Option Five)
- The Exit option allows the user to end the program.


## User Input Validation 
- The input validation checks has the user entered valid data and the correct amount of digits.
- If the incorrect amount of digits is entered the user an error message will be displayed in the terminal.

![User input validation (Three digits)](assets/images/readme_images/user_input_validation_count.PNG)
![User input validation (One digit)](assets/images/readme_images/user_input_validation_one_digit.PNG)

- Input validation checks if alphabetical characters have been used.
- If alphabetical characters are used instead of numbers an error message will be displayed in the terminal. 

![User input validation (Alphabetical)](assets/images/readme_images/user_input_validation_alphabetical.PNG)

- Input validation checks if special characters and spaces are used.
- If special characters are used an error message will be displayed in the terminal. 

![User input validation (Special characters)](assets/images/readme_images/special_character_validation.PNG)


## Languages
- Python 3

## Frameworks and Tools
- gitHub
- Gitpod
- Git

## Libraries 
- The gspread library is used to interact with google sheets.
- The sys library is used for the exit function in the program.
- The time library is used to make time stamps for the employees cloking in and out.

## Bugs
| **Feature / Function** | **Expected Result** | **Actual Result** | **Action** |
|-------------|------------|---------------------|-------------------|
| find_last_employee_entry()| It would count employee numbers | ValueError: invalid literal for int() | The first cell was a heading. This was fixed by using indexing to begin at the second cell [1:]|
|transfer_of_data()| To revieve input from the user and update google sheets | TypeError: can only concatenate list (not "str") to list | To concatenate the two variables I needed to format the string type into a list. Example: csv_result = employee_details + clockin_time
|userFeedback()| This function would take feedback from the user and update the user_feedback worksheet| gspread.exceptions.APIError: {'code': 400, 'message': 'Invalid value at \'data.values[0]\'| To change data to the correct data type the user input was passed into a list|

## Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Options Menu| Run the program, choose all menu options one by one| That the option selected by the user would execute.| As expected |
| Clock in | Type in a correct employee number | Update Google Sheets with  employee number, name and time of clock in | As expected |
| Clock out | Type in a correct employee number | Find where the employee signed in Update Google Sheets clock out cell with the current time | As expected |
| Give Feedback | Type in feedback | Feedback is recived, user_feedback worksheet in google sheets is updated | As expected|
| Exit | Choose the exit option | This will terminate the program | As expected |
| User input validation | Takes user input to validate | Checks to see if the user has entered a valid input | As expected |

## Validator Testing 
### PEP8 Validation
- The PEP8 Valitator has resulted in no errors or warnings

![PEP8 Validator](assets/images/readme_images/pep_validation.PNG)

## Deployment
Heroku was used for the deployment of this program.
1. In the workspace terminal command line: "pip3 freeze > requirements.txt"
2. Create account on Heroku
3. On the dashboard page, select "create new app"
4. Click create app
5. Go to the "settings" tab, find "Config Vars" enter "Creds" into the key field and copy the contents for the creds.json file into the value field
6. In setting find add buid packs to app
    1. python
    2. node.js
6. Scroll up to the navigation menu and find "deploy", select GitHub as deployment method
7. In the Deployment Method section select Gitub or connect to GitHub
8. In the "Connect to GitHub, searh the desired repository
9. Enable automatic deploys and then deploy branch
10. Once deployed click on "View" to open aplication

## Credits
### Code
- To implement time into the program I used https://www.programiz.com/python-programming/datetime/current-time 
- To find additonal features working with Google Sheets I used https://www.youtube.com/watch?v=yPQ2Gk33b1U&ab_channel=PrettyPrinted 
- To validate user input I used the isdigit() function found from https://pynative.com/python-check-user-input-is-number-or-string/#:~:text=To%20check%20if%20the%20input%20string%20is%20an%20integer%20number,using%20the%20int()%20constructor.&text=To%20check%20if%20the%20input%20is%20a%20float%20number%2C%20convert,using%20the%20float()%20constructor.



