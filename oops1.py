# initiate a class
class employee:
    # constructor
    def __init__(self):
        self.id=123
        self.salary=50000
        self.designation="Software Engineer"
    
    def travel(self,destination):
        print(f"employee is travelling to {destination}")



# object/instance
sam=employee()
print(type(sam))
print(sam.id)
sam.travel("Roorkee")
