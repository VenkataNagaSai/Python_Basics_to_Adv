# Define the Employee class
class Employee:
    # Class variable: shared among all Employee objects
    empCount = 0

    # Constructor: called automatically when an object is created
    def __init__(self, name):
        # Instance variable: unique to each Employee object
        self.name = name

        # Increment the class variable whenever a new object is created
        Employee.empCount += 1

# Create an Employee object with the name "Zara"
emp1 = Employee("Zara")

# Display the instance variable and the shared class variable
print("Instance name:", emp1.name, "| Class count:", Employee.empCount)
