# domain/employee_entity.py
class Employee:
    """Represents an employee with id, name, and position."""
    def __init__(self, id: int, name: str, position: str):
        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        self.id = id
        self.name = name
        self.position = position