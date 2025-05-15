# tests/test_employee_entity.py
import pytest
from domain.employee_entity import Employee

# ----- Employee Entity Tests -----

def test_employee_initialization():
    # Test that an Employee instance stores the correct attributes
    emp = Employee(1, "Alice", "Engineer")
    assert emp.id == 1
    assert emp.name == "Alice"
    assert emp.position == "Engineer"

def test_employee_with_mutation():
    # Test that Employee attributes can be changed after initialization implying mutability
    emp = Employee(42, "Bob", "Manager")
    assert emp.id == 42
    assert emp.name == "Bob"
    assert emp.position == "Manager"
    
    # Change attributes
    emp.name = "Robert"
    emp.position = "Senior Manager"
    
    assert emp.name == "Robert"
    assert emp.position == "Senior Manager"

def test_employee_invalid_id_type():
    # Test that passing a non-integer ID raises a TypeError or does not set id as int
    # Since the Employee class does not enforce types, let's test behavior explicitly
    with pytest.raises(TypeError):
        emp = Employee("not-an-int", "Charlie", "Analyst")
