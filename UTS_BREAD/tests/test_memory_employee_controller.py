# tests/test_memory_employee_controller.py
import pytest
from data.memory_employee_controller import MemoryEmployeeController
from domain.employee_entity import Employee

@pytest.fixture
def mem_controller():
    return MemoryEmployeeController()

def test_memory_add_and_get(mem_controller):
    # Add an employee and retrieve it
    emp = Employee(1, "Alice", "Engineer")
    mem_controller.add_employee(emp)
    assert mem_controller.get_employee(1) == emp

def test_memory_update(mem_controller):
    # Update an existing employee's position
    emp = Employee(2, "Bob", "Manager")
    mem_controller.add_employee(emp)
    updated = Employee(2, "Bob", "Director")
    mem_controller.update_employee(updated)
    assert mem_controller.get_employee(2).position == "Director"

def test_memory_delete_and_list(mem_controller):
    # Delete an employee and check the remaining list
    emp1 = Employee(3, "Carol", "Analyst")
    emp2 = Employee(4, "Dave", "Designer")
    mem_controller.add_employee(emp1)
    mem_controller.add_employee(emp2)
    mem_controller.delete_employee(3)
    remaining = mem_controller.list_employees()
    assert emp1 not in remaining and emp2 in remaining
