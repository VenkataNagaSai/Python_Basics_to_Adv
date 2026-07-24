# 1. Abstraction & Base Blueprint
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    # A method meant to be overridden (Polymorphism)
    def perform_daily_duty(self):
        pass

# 2. Inheritance (Student inherits from Person)
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number) # Inheriting name and ID setup
        self.major = major
        self.__gpa = 0.0  # 3. Encapsulation (Hidden attribute)

    # 4. Polymorphism (Student's specific version of the duty)
    def perform_daily_duty(self):
        print(f"{self.name} is studying for {self.major} exams.")

    # Controlled access to the hidden __gpa attribute
    def set_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            print(f"GPA securely updated to {self.__gpa}")
        else:
            print("Invalid GPA!")

# 2. Inheritance (Professor inherits from Person)
class Professor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    # 4. Polymorphism (Professor's specific version of the duty)
    def perform_daily_duty(self):
        print(f"Professor {self.name} is teaching a {self.department} class.")

# --- Using the Objects ---

print("--- Creating Objects ---")
alice = Student("Alice", 101, "Computer Science")
dr_smith = Professor("Dr. Smith", 999, "VLSI Engineering")

print("\n--- Testing Polymorphism ---")
alice.perform_daily_duty()
dr_smith.perform_daily_duty()

print("\n--- Testing Encapsulation ---")
alice.set_gpa(3.8)
# print(alice.__gpa) # This would crash the script because the data is hidden!
