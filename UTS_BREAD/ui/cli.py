# ui/cli.py
from application.employee_usecase import EmployeeUseCase
from data.memory_employee_controller import MemoryEmployeeController

def main():
    # Set up the in-memory data controller and inject it into the use case
    controller = MemoryEmployeeController()
    usecase = EmployeeUseCase(controller)

    # Start the command-line interface loop
    while True:
        print("\nChoose operation: add, read, edit, delete, browse, exit")
        choice = input("Your choice: ").strip().lower()
        
        # --- ADD OPERATION ---
        if choice == "add":
            try:
                id = int(input("\nEnter ID: "))
                existing = usecase.read_employee(id)
                if existing is not None:
                    print(f"Employee with ID {id} already exists. Cannot add duplicate.")
                else:
                    name = input("Enter name: ").strip()
                    position = input("Enter position: ").strip()
                    emp = usecase.add_employee(id, name, position)
                    print(f"\nAdded: {emp.id}, {emp.name}, {emp.position}")
            except Exception as e:
                print(f"Error: {e}")

        # --- READ OPERATION ---
        elif choice == "read":
            try:
                id = int(input("\nEnter ID: "))
                # Look up employee by ID
                emp = usecase.read_employee(id)
                if emp:
                    print(f"\nFound: {emp.id}, {emp.name}, {emp.position}")
                else:
                    print("\nEmployee not found.")
            except Exception as e:
                print(f"Error: {e}")

        # --- EDIT OPERATION ---
        elif choice == "edit":
            try:
                id = int(input("\nEnter ID: "))
                # Check if employee exists before editing
                existing = usecase.read_employee(id)
                if existing is None:
                    print("\nNo Employee Found.")
                else:
                    name = input("Enter new name: ").strip()
                    position = input("Enter new position: ").strip()
                    # Update the employee details
                    emp = usecase.edit_employee(id, name, position)
                    print(f"\nUpdated: {emp.id}, {emp.name}, {emp.position}")
            except Exception as e:
                print(f"Error: {e}")

        # --- DELETE OPERATION ---
        elif choice == "delete":
            try:
                id = int(input("\nEnter ID: "))
                # Check if the employee exists before trying to delete
                employee = usecase.read_employee(id)
                if employee is None:
                    print("\nNo employees found.")
                else:
                    usecase.delete_employee(id)
                    print(f"\nDeleted employee with ID {id}")
            except Exception as e:
                print(f"Error: {e}")

        # --- BROWSE OPERATION ---
        elif choice == "browse":
             # List all employees
            employees = usecase.browse_employees()
            if employees:
                print("\nEmployees:")
                for emp in employees:
                    print(f"- {emp.id}: {emp.name} ({emp.position})")
            else:
                print("\nNo employees found.")

        # --- EXIT ---
        elif choice == "exit":
            print("Exiting.")
            break

        # --- INVALID CHOICE ---
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
