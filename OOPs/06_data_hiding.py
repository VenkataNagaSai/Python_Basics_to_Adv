# Define the Counter class
class Counter:

    # Private (name-mangled) class variable
    # Prefixing with '__' makes it inaccessible directly from outside the class
    Count = 0
    __secretCount = 0

    # Method to increment and display the private counter
    def count(self):
        # Access and update the private variable within the class
        self.__secretCount += 1
        self.Count += 1

        # Display the updated count
        print("Secret Count:", self.__secretCount)
        print("Count:", self.Count)

# Create an object of the Counter class
c = Counter()

# Call the method to increment and display the counter
c.count()

# Attempting to access the private variable directly will raise an AttributeError
# because Python performs name mangling for variables prefixed with '__'.
# print(c.__secretCount)   # This would throw an error!
# print(c.Count)   # This would throw an error!
