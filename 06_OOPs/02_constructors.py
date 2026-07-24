# Define the Employee class
class Employee:

    # Constructor: automatically called when an object is created
    def __init__(self, name, salary):
        # Display a message indicating that the constructor is executed
        print(f"Constructor called for {name}")

        # Initialize instance variables with the provided values
        self.name = name
        self.salary = salary

# Create an Employee object
# This automatically invokes the constructor (__init__)
emp1 = Employee("Manni", 5000)
