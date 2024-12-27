# Basic Social Media platform
class chatapp:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

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
            pass
        elif user_input=='4':
            pass
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



obj=chatapp()
