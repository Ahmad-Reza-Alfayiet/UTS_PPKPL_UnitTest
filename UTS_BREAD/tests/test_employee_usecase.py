# tests/test_employee_usecase.py
import pytest
from data.memory_employee_controller import MemoryEmployeeController
from application.employee_usecase import EmployeeUseCase

@pytest.fixture
def usecase():
    return EmployeeUseCase(MemoryEmployeeController())

# ----- ADD Employee Tests -----

def test_add_and_read_employee(usecase):
    # 1. Add a single employee and verify it's retrievable
    usecase.add_employee(1, "Alice", "Engineer")
    emp = usecase.read_employee(1)
    assert emp is not None
    assert emp.id == 1
    assert emp.name == "Alice"
    assert emp.position == "Engineer"

def test_add_duplicate_id_raises_error(usecase):
    # 2. Adding an employee with an existing ID should raise an exception
    usecase.add_employee(2, "Bob", "Manager")
    with pytest.raises(ValueError) as exc:
        usecase.add_employee(2, "Bobby", "Senior Manager")
    assert "already exists" in str(exc.value)

def test_add_multiple_employees(usecase):
    # 3. Add multiple employees and verify all are present
    usecase.add_employee(3, "Carol", "Analyst")
    usecase.add_employee(4, "Dave", "Designer")
    emp3 = usecase.read_employee(3)
    emp4 = usecase.read_employee(4)
    assert emp3.name == "Carol"
    assert emp4.name == "Dave"

# ----- READ Employee Tests -----

def test_read_existing_employee(usecase):
    # 1. Read after adding should return the employee
    usecase.add_employee(5, "Eve", "Tester")
    emp = usecase.read_employee(5)
    assert emp is not None
    assert emp.id == 5

def test_read_nonexistent_employee(usecase):
    # 2. Reading a non-existent ID should return None
    emp = usecase.read_employee(999)
    assert emp is None

def test_read_after_deletion(usecase):
    # 3. Read should return None after deletion
    usecase.add_employee(6, "Frank", "Dev")
    usecase.delete_employee(6)
    emp = usecase.read_employee(6)
    assert emp is None

# ----- EDIT Employee Tests -----

def test_edit_existing_employee(usecase):
    # 1. Edit an existing employee's details
    usecase.add_employee(7, "Grace", "Intern")
    usecase.edit_employee(7, "Grace", "Junior Engineer")
    emp = usecase.read_employee(7)
    assert emp.position == "Junior Engineer"

def test_edit_nonexistent_employee(usecase):
    # 2. Editing a non-existent employee should do nothing (no new entry)
    usecase.edit_employee(8, "Heidi", "Lead")
    emp = usecase.read_employee(8)
    assert emp is None

def test_edit_multiple_times(usecase):
    # 3. Multiple edits in a row result in final state
    usecase.add_employee(9, "Ivan", "Analyst")
    usecase.edit_employee(9, "Ivan", "Senior Analyst")
    usecase.edit_employee(9, "Ivan", "Principal Analyst")
    emp = usecase.read_employee(9)
    assert emp.position == "Principal Analyst"

# ----- DELETE Employee Tests -----

def test_delete_existing_employee(usecase):
    # 1. Delete an existing employee
    usecase.add_employee(10, "Judy", "HR")
    usecase.delete_employee(10)
    assert usecase.read_employee(10) is None

def test_delete_nonexistent_employee(usecase):
    # 2. Deleting non-existent ID should not raise and not affect others
    usecase.delete_employee(9999)
    usecase.add_employee(11, "Karl", "Ops")
    assert usecase.read_employee(11) is not None

def test_delete_then_readd(usecase):
    # 3. Delete then re-add should succeed
    usecase.add_employee(12, "Liam", "Support")
    usecase.delete_employee(12)
    usecase.add_employee(12, "Liam", "Support")
    assert usecase.read_employee(12) is not None

# ----- BROWSE Employee Tests -----

def test_browse_empty(usecase):
    # 1. Browse on empty store returns empty list
    assert usecase.browse_employees() == []

def test_browse_after_add(usecase):
    # 2. Browse lists all added employees
    usecase.add_employee(13, "Mia", "QA")
    usecase.add_employee(14, "Nate", "DevOps")
    all_emps = usecase.browse_employees()
    ids = [e.id for e in all_emps]
    assert 13 in ids and 14 in ids

def test_browse_after_delete(usecase):
    # 3. Browse reflects deletions
    usecase.add_employee(15, "Olivia", "Manager")
    usecase.delete_employee(15)
    all_emps = usecase.browse_employees()
    assert 15 not in [e.id for e in all_emps]