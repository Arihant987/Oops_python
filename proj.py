# Basic Social Media platform
class chatapp:

    # Static attribute directly accesible by "class only"
    __user_id=0

    def __init__(self):
        self.__prvt="private attribute"
        self.id=chatapp.__user_id
        chatapp.__user_id+=1   
        self.username=''
        self.password=''
        self.loggedin=False
        # self.menu()

    # Getter and Setter  
    @staticmethod
    def get_id():
        return chatapp.__user_id
    
    def set_id(value):
        chatapp.__user_id=value

    def get_name(self):
        return self.__prvt
    
    def set_name(self,value):
        self.__prvt=value

    def menu(self):
        user_input=input('''Welcome to Chatapp !! How would you like to proceed ?
                         1. Press 1 to signup
                         2. Press 2 to login
                         3. Press 3 to write a post 
                         4. Press 4 to write a message to friend
                         5. Press any other key to logout ''')   

        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.login()
        elif user_input=='3':
            self.write_post()
        elif user_input=='4':
            self.write_message()
        else:
            exit()

    def signup(self):
        email=input("enter your email: ")
        pwd=input("enter your password: ")   
        self.username=email
        self.password=pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()   

    def login(self):
        if self.username=='' and self.password=='':
            print("First do signup !!")
        else:
            email=input("enter your email: ")
            pwd=input("enter your password: ") 
            if(self.username==email and self.password==pwd):
                print("You have logged in successfully !!")
                self.loggedin=True
            else:
                print("Invalid credentials !!")
        print("\n")
        self.menu()

    def write_post(self):
        if(self.loggedin):
            post=input("Write your post: ")
            print(f"Your post is {post}")
        else:
            print("Please login first !!")
        print("\n")
        self.menu()  

    def write_message(self):
        if(self.loggedin):
            friend=input("Enter your friend name: ")
            message=input("Write your message: ")
            print(f"Your message to {friend} is {message}")       

        else:
            print("Please login first !!")
        print("\n")
        self.menu()



# user=chatapp()
