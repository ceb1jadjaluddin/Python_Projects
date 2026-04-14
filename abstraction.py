# -------------------------------
# ABSTRACTION EXAMPLE IN PYTHON
# -------------------------------

from abc import ABC, abstractmethod

# Parent class (Abstract Class)
class Animal(ABC):

    # Abstract method (no implementation here)
    # Child classes MUST implement this method
    @abstractmethod
    def make_sound(self):
        pass

    # Regular method (already has implementation)
    def sleep(self):
        print("This animal is sleeping")


# Child class that inherits from Animal
class Dog(Animal):

    # Implementing the abstract method
    def make_sound(self):
        print("Dog says: Woof Woof")


# -------------------------------
# Creating object from child class
# -------------------------------
dog1 = Dog()

# Using implemented abstract method (from child class)
dog1.make_sound()

# Using regular method (from parent class)
dog1.sleep()
