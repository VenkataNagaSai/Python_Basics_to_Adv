# Define the Employee class
class Employee:

    # Constructor: initializes the object with the employee's name
    def __init__(self, name):
        # Store the employee's name as an instance variable
        self.name = name

    # Instance method
    # 'self' refers to the current object and must be the first parameter
    def display(self):
        # Display the employee's name
        print("Employee Name:", self.name)

# Create an Employee object
emp1 = Employee("Zara")

# Call the instance method using the object
emp1.display()
