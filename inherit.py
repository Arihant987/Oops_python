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
        # if there is no name inside child class then using super it will not work one way is to call super().__init__(name) in child class constructor
        print(f"my name is {self.name}")         

animal_obj=animal("cow")
animal_obj.speak()
dog_obj=dog("libra")
print(dog_obj.speak())       