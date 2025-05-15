# tests/test_employee_controller.py
import pytest
from domain.employee_controller import EmployeeController

def test_interface_instantiation():
    # EmployeeController is abstract; instantiating should fail
    with pytest.raises(TypeError):
        EmployeeController()

def test_interface_methods_exist():
    # Verify that the abstract methods are defined in the interface
    methods = [func for func in dir(EmployeeController) if not func.startswith('_')]
    expected = ['add_employee', 'delete_employee', 'get_employee',
                'list_employees', 'update_employee']
    for method in expected:
        assert method in methods
