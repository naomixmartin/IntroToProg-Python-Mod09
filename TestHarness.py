# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A main module for testing module data
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script in Listing 10
# naomimartin, 09.02.2022, modified script to test modules
# ---------------------------------------------------------- #

if __name__ == "__main__":
    import DataClasses as D # naomimartin: imports all classes in DataClasses module with alias D
    import ProcessingClasses as P  # naomimartin: import the ProcessingClasses module with alias P
    from IOClasses import EmployeeIO as Io  # naomimartin: import EmployeeIO class from IOClasses module with alias Io
else:
    raise Exception("This file was not created to be imported")


# Test Person class in DataClasses module
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
pLstTable = [objP1, objP2]
print("Person data:")
for row in pLstTable:
    print(row.to_string(), type(row))
print() # naomimartin: extra line for looks

# Test Employee class in DataClasses module
objEmp1 = D.Employee(1,"Bob","Smith")
objEmp2 = D.Employee(2,"Sue", "Jones")
lstTable = [objEmp1, objEmp2]
print("Employee data:")
for row in lstTable:
    print(row.to_string(), type(row))
print() # naomimartin: extra line for looks



# Test ProcessingClasses module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)  # naomimartin: saves data to file
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")  # naomimartin: loads in data to test processor
lstTable.clear()
for line in lstFileData:
    lstTable.append(D.Employee(line[0], line[1], line[2].strip()))  # naomimartin: creates and appends to lstTable a
    # new object with the attributes as defined in each line of the lstFileData table, loaded in from EmployeeData.txt
print("Data from file: ")
for row in lstTable:
    print(row.to_string(), type(row))
print()

# Test IOClasses module
print("Test print menu items:")
Io.print_menu_items()

print("Test input menu options:\n")
choice = Io.input_menu_options()
print("Inputted choice: ", choice,"\n")

print("Test print current items in list:\n")
Io.print_current_list_items(lstTable)

print("Test input employee data:\n")
emp = Io.input_employee_data()
print("Inputted employee data: ",emp)
