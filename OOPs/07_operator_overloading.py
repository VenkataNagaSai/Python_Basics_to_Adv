# Define the Vector class
class Vector:

    # Constructor: initializes the vector components
    def __init__(self, a, b):
        # Store the x and y components of the vector
        self.a, self.b = a, b

    # Overload the '+' operator
    # This method is called when two Vector objects are added
    def __add__(self, other):
        # Return a new Vector whose components are the sum
        # of the corresponding components of both vectors
        return Vector(self.a + other.a, self.b + other.b)

    # Overload the str() function
    # This method defines how the object is displayed when printed
    def __str__(self):
        return f"Vector({self.a}, {self.b})"

# Create two Vector objects
v1 = Vector(2, 10)
v2 = Vector(5, -2)

# Add the two vectors using the overloaded '+' operator
# The result is automatically displayed using the __str__() method
print("Added Vectors:", v1 + v2)
