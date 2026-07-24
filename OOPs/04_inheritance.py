# Define the Parent class
class Parent:

    # Method belonging to the Parent class
    def parentMethod(self):
        print("Calling parent method")

# Define the Child class that inherits from Parent
class Child(Parent):

    # Method specific to the Child class
    def childMethod(self):
        print("Calling child method")

# Create an object of the Child class
c = Child()

# Call the method defined in the Child class
c.childMethod()

# Call the inherited method from the Parent class
# The Child object can access Parent methods through inheritance
c.parentMethod()
