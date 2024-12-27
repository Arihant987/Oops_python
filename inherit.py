# Base class/parent class
class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} is speaking")  

# Derived class/child class 
# Can not access the private members of the Base class
class dog(animal):
    # Constructor overriding
    def __init__(self,name):
        self.name=name
        print("dog class constructor")

    # Method overriding
    def speak(self):
        super().speak()
        print(f"my name is {self.name}")         

animal_obj=animal("cow")
animal_obj.speak()
dog_obj=dog("libra")
print(dog_obj.speak())       