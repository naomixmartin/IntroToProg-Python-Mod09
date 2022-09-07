# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# naomimartin, 09.03.2022, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

lstTable = []  # naomimartin: declare empty list to store employee object data
lstFileData = []  # naomimartin: declare empty list to load in employee data from EmployeeData.txt file

if __name__ == "__main__":
    import DataClasses as D # naomimartin: imports all classes in DataClasses module with alias D
    import ProcessingClasses as P  # naomimartin: import the ProcessingClasses module with alias P
    from IOClasses import EmployeeIO as Io  # naomimartin: import EmployeeIO class from IOClasses module with alias Io
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
for line in lstFileData:
    lstTable.append(D.Employee(line[0], line[1], line[2].strip()))
Io.print_current_list_items(lstTable)

while True:
    # Show user a menu of options
    Io.print_menu_items()
    # Get user's menu option choice
    choice = Io.input_menu_options()
    # Show user current data in the list of employee objects

    if choice == "1":
        Io.print_current_list_items(lstTable)

    # Let user add data to the list of employee objects
    elif choice == "2":
        emp = Io.input_employee_data()
        lstTable.append(emp)
        print("\nYour inputted employee data: ", emp)
    # Let user save current data to file
    elif choice == "3":
        P.FileProcessor.save_data_to_file("EmployeeData.txt",lstTable)

    # Let user exit program
    elif choice == "4":
        break

    # Re-attempt to obtain user input if no valid input is given
    else:
        print("Please select a valid menu option.")