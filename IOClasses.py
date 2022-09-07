# ---------------------------------------------------------- #
# Title: IO Classes
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030, Created script in Listing 11
# naomimartin, 09.03.2022, modified script to complete IO Classes module
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to be ran by itself")
else:
    import DataClasses as D


class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items(): prints a menu of options
        input_menu_options(): obtains user input for menu option choice -> (string) with numerical value for choice
        print_current_list_items(list_of_rows): creates new employee objects from specified list and prints to screen
        input_employee_data(): obtains user input for employee_id, first_name, and last_name attributes -> (object)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        naomimartin, 09.03.2022, updated methods descriptions in docstring
    """

    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data 
        3) Save employee data to File
        4) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: (string) with user input choice
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current item employees are: *******")
        try:
            for row in list_of_rows:
                print(row.to_string())  # naomimartin: modified to simplify code
            if not list_of_rows:
                raise Exception  # naomimartin: raise exception if list_of_rows is empty
        except Exception:
            print("\nThere are no items currently in the list.\n")  # naomimartin: if there are no items in the list at
            # the start of the program
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_employee_data():
        """ Gets data for an employee object while simultaneously testing for valid input

        :return: (employee) object with input data
        """
        while True:  # naomimartin: tests to ensure that employee ID input is valid before continuing
            try:
                employee_id = (input("What is the employee Id? - ").strip())
                if employee_id.isnumeric() == False:  # naomimartin: raises custom exception if input is not numeric
                    raise Exception("Invalid input: employee ID must be a number. Please try again. \n")
                else:
                    break
            except Exception as e:
                print(e)
                continue

        while True:  # naomimartin: tests to ensure that first name input is valid before continuing
            try:
                first_name = str(input("What is the employee First Name? - ").strip())
                if first_name.isnumeric() == True:  # naomimartin: raises custom exception if input is numeric
                    raise Exception("Invalid input: first name cannot be a number. Please try again. \n")
                else:
                    break
            except Exception as e:
                print(e)
                continue

        while True:  # naomimartin: tests to ensure that last name input is valid before continuing
            try:
                last_name = str(input("What is the employee Last Name? - ").strip())
                if last_name.isnumeric() == True:  # naomimartin: raises custom exception if input is numeric
                    raise Exception("Invalid input: last name cannot be a number. Please try again. \n")
                else:
                    break
            except Exception as e:
                print(e)
                continue
        emp = D.Employee(employee_id, first_name, last_name)  # naomimartin: if all input is valid, an employee object
        # is created
        return emp

