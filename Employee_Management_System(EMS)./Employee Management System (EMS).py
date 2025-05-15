#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    """Class to represent an Employee"""
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display(self):
        """Returns employee details as a formatted string"""
        return f"{self.emp_id:<10}{self.name:<15}{self.age:<5}{self.department:<15}{self.salary:<10}"

class EmployeeManagementSystem:
    """Class to manage Employee records"""
    def __init__(self):
        # Initializing with sample employee data
        self.employees = {
            101: Employee(101, "Gaurav", 27, "HR", 50000),
            102: Employee(102, "Amit", 30, "IT", 70000),
            103: Employee(103, "Neha", 25, "Finance", 60000)
        }

    def add_employee(self):
        """Method to add a new employee"""
        while True:
            try:
                emp_id = int(input("Enter Employee ID: "))
                if emp_id in self.employees:
                    print("Employee ID already exists...! Try a different ID.")
                    continue
                break
            except ValueError:
                print("Invalid input! Employee ID should be a number.")

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = int(input("Enter Employee Salary: "))

        self.employees[emp_id] = Employee(emp_id, name, age, department, salary)
        print(f"Employee {name} added successfully!")

    def view_employees(self):
        """Method to display all employees"""
        if not self.employees:
            print("No employees available.")
            return

        print("\nEmployee List:")
        print("-" * 50)
        print(f"{'ID':<10}{'Name':<15}{'Age':<5}{'Department':<15}{'Salary':<10}")
        print("-" * 50)
        
        for employee in self.employees.values():
            print(employee.display())
        
        print("-" * 50)

    def search_employee(self):
        """Method to search for an employee by ID"""
        try:
            emp_id = int(input("Enter Employee ID to search: "))
            if emp_id in self.employees:
                employee = self.employees[emp_id]
                print("\nEmployee Found:")
                print(f"ID: {employee.emp_id}")
                print(f"Name: {employee.name}")
                print(f"Age: {employee.age}")
                print(f"Department: {employee.department}")
                print(f"Salary: {employee.salary}")
            else:
                print("Employee not found!")
        except ValueError:
            print("Invalid input! Employee ID should be a number.")

    def main_menu(self):
        """Method to handle user interaction"""
        while True:
            print("\nWelcome To The Employee Management System")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search for Employee")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                print("Thank you for using the Employee Management System....!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

# Running EMS
if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.main_menu()



