from abc import ABC, abstractmethod


class Animal(ABC):
    def walk(self):
        print("Every animal walks")
        return

    @abstractmethod
    def speak(self):
        pass


class Tiger(Animal):
    def speak(self):  # implementing abstract method
        print("Tiger Roars")


# a1 = Animal() #ERROR
t1 = Tiger()
t1.speak()
t1.walk()
