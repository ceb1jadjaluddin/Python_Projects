# -------------------------------
# Encapsulation Example in Python
# -------------------------------

class Student:
    # Constructor method
    def __init__(self, name, age, grade):
        # Public attribute (accessible anywhere)
        self.name = name

        # Protected attribute (convention: single underscore)
        # Should not be accessed directly outside the class or subclasses
        self._age = age

        # Private attribute (double underscore)
        # Strongly restricted (name mangling happens internally)
        self.__grade = grade

    # Public method to access private attribute safely
    def get_grade(self):
        return self.__grade

    # Public method to update private attribute safely
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade value")

    # Protected method (convention)
    def _display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Grade: {self.__grade}")


# -------------------------------
# Creating an object
# -------------------------------
student1 = Student("Alice", 20, 85)

# Accessing public attribute
print("Public Name:", student1.name)

# Accessing protected attribute (allowed but not recommended)
print("Protected Age:", student1._age)

# Accessing private attribute directly (NOT allowed - will fail if uncommented)
# print(student1.__grade)

# Correct way: using getter method
print("Private Grade (via method):", student1.get_grade())

# Updating private attribute safely
student1.set_grade(90)

# Using protected method (still possible but discouraged)
student1._display_info()
