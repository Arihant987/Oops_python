from proj import chatapp

user=chatapp()
print(user.get_name())
user.set_name("public attribute")
print(user.get_name())
print(user.id)

# static method only accessible through class name
chatapp.set_id(15)
user2=chatapp()
print(user2.id)

user3=chatapp()
print(user3.id)
