# domain/employee_controller.py
from abc import ABC, abstractmethod
from .employee_entity import Employee

class EmployeeController(ABC):
    """Interface (gateway) for employee data operations in the domain layer."""
    @abstractmethod
    def add_employee(self, employee: Employee) -> None:
        """Add a new employee."""
        pass

    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        """Retrieve an employee by ID."""
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> None:
        """Update an existing employee."""
        pass

    @abstractmethod
    def delete_employee(self, employee_id: int) -> None:
        """Delete an employee by ID."""
        pass

    @abstractmethod
    def list_employees(self) -> list:
        """List all employees."""
        pass