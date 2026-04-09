# Parent class
class Organism:
    def __init__(self, name, species, legs, arms):
        self.name = name
        self.species = species
        self.legs = legs
        self.arms = arms

    # Parent method (this will be overridden by child classes)
    def describe(self):
        return f"{self.name} is a {self.species} with {self.legs} legs and {self.arms} arms."


# Child class 1
class Human(Organism):
    def __init__(self, name, species, legs, arms, language, job):
        super().__init__(name, species, legs, arms)
        self.language = language
        self.job = job

    # Polymorphism: overriding parent method
    def describe(self):
        return f"{self.name} is a human who speaks {self.language} and works as a {self.job}."


# Child class 2
class Dog(Organism):
    def __init__(self, name, species, legs, arms, breed, sound):
        super().__init__(name, species, legs, arms)
        self.breed = breed
        self.sound = sound

    # Polymorphism: overriding parent method
    def describe(self):
        return f"{self.name} is a {self.breed} dog that says {self.sound}."


# Creating objects
human = Human("Alice", "Homo Sapiens", 2, 2, "English", "Developer")
dog = Dog("Buddy", "Canis Lupus", 4, 0, "Golden Retriever", "Woof")

# Output results
print(human.describe())
print(dog.describe())