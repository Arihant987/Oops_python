# initiate a class
class employee:
    # constructor
    def __init__(self):
        self.__name="private"
        self.id=123
        self.salary=50000
        self.designation="Software Engineer"
    
    def travel(self,destination):
        print(f"employee is travelling to {destination}")



# object/instance
sam=employee()
sam.id=456
sam.llm="Chatgpt"

print(sam.id)
# print(sam.__name) is a private variable
print(sam._employee__name)
sam.travel("Roorkee")
