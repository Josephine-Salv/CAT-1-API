class Employee:
    def _init_(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary updated to {self.salary}.")


class Department:
    def _init_(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary}")
        return total_salary

    def display_all_employees(self):
        if self.employees:
            print(f"Employees in {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in {self.department_name} department.")