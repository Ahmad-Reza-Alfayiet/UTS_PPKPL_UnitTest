# application/employee_usecase.py
from domain.employee_controller import EmployeeController
from domain.employee_entity import Employee

class EmployeeUseCase:
    """Application logic for managing employees (BREAD operations)."""
    def __init__(self, controller: EmployeeController):
        self.controller = controller  # e.g. MemoryEmployeeController

    def add_employee(self, id: int, name: str, position: str):
        """Create and add a new employee. Raise error if ID already exists."""
        if self.controller.get_employee(id) is not None:
            raise ValueError(f"Employee with ID {id} already exists")
        
        employee = Employee(id, name, position)
        self.controller.add_employee(employee)
        return employee

    def read_employee(self, id: int):
        """Retrieve an employee by id."""
        return self.controller.get_employee(id)

    def edit_employee(self, id: int, name: str, position: str):
        """Update an existing employee's details."""
        employee = Employee(id, name, position)
        self.controller.update_employee(employee)
        return employee

    def delete_employee(self, id: int):
        """Delete an employee by id."""
        self.controller.delete_employee(id)

    def browse_employees(self):
        """List all employees."""
        return self.controller.list_employees()
    