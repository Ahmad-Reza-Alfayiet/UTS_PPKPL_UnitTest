# data/memory_employee_controller.py
from domain.employee_controller import EmployeeController
from domain.employee_entity import Employee

class MemoryEmployeeController(EmployeeController):
    """In-memory implementation of EmployeeController."""
    def __init__(self):
        self.employees = {}  # Dict mapping id -> Employee

    def add_employee(self, employee: Employee):
        # Store the employee by id
        self.employees[employee.id] = employee

    def get_employee(self, employee_id: int):
        # Return the employee or None if not found
        return self.employees.get(employee_id)

    def update_employee(self, employee: Employee):
        # Only update if the employee exists
        if employee.id in self.employees:
            self.employees[employee.id] = employee

    def delete_employee(self, employee_id: int):
        # Remove the employee if present
        if employee_id in self.employees:
            del self.employees[employee_id]

    def list_employees(self):
        # Return all employees as a list
        return list(self.employees.values())
