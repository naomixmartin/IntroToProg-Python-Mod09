# ---------------------------------------------------------- #
# Title: Data Classes
# Description: A module of data classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030, Wrote script in Listing06
# naomimartin, 09.02.2022, modified script to complete DataClasses module
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class Person:
    """Stores data about a person:

    properties:
        first_name: (string) with the person's first name
        last_name: (string) with the person's last name

    methods:
        to_string() -> comma separated product data (alias for __str__())

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        naomimartin, 09.02.2022, modified class and updated methods descriptions in docstring
    """

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # -- Attributes --
        self.__first_name = first_name
        self.__last_name = last_name

    # -- Properties --
    @property
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.first_name + ', ' + self.last_name


class Employee(Person):
    """ Stores data about an employee:

    properties:
        employee_id: (string) with numerical value of employee's ID
        first_name: (string) with the person's first name, inherited from person class
        last_name: (string) with the person's last name, inherited from person class

    methods:
        to_string() -> comma separated product data (alias for __str__())

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        naomimartin, 09.02.2022, modified class
    """

    # -- Constructor --
    def __init__(self, employee_id, first_name, last_name):
        # -- Attributes --
        super().__init__(first_name, last_name)  # naomimartin: attributes inherited from the parent (super) class
        self.__employee_id = employee_id


    # -- Properties --
    @property
    def employee_id(self):
        return str(self.__employee_id).strip()

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value

    # -- Methods --
    def to_string(self):  # Overrides the original method (polymorphic)
        """ Explicitly returns a string with this object's data """
        # Linking to self.__str__() does not work with inheritance
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ', ' + data

    def __str__(self):  # Overrides the original method (polymorphic)
        """ Implicitly returns field data """
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ', ' + data

