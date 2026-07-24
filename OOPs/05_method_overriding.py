# Define the Parent class
class Parent:

    # Method defined in the Parent class
    def myMethod(self):
        print("Parent method")

# Define the Child class that inherits from Parent
class Child(Parent):

    # Override the Parent's myMethod()
    # This method replaces the inherited version
    def myMethod(self):
        print("Overridden Child method")

# Create an object of the Child class
c = Child()

# Call the overridden method
# The Child class version is executed instead of the Parent class version
c.myMethod()
