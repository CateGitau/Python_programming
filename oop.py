# class Dog():
#     species = "Canabis"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# miles = Dog("Miles", 4)
# print(miles.description())
# print(miles.speak("woof woof"))

# class Car():
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage

#     def __str__(self):
#         return f"the {self.color} car has {self.mileage:,} miles"


# blue_car = Car("blue", 20_000)
# red_car = Car("red", 30_000)

# print(blue_car)
# print(red_car)


#creating new child classes of the Dog class

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass

miles = JackRusselTerrier("miles", 4)

print(miles.speak("woof woof"))
print(miles.speak())
print(isinstance(miles, Dog))