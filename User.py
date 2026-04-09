# Parent class
class User:
    # Define the attributes of the class
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    # Define the methods of the class
    def login(self):
        # Ask user for login credentials
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")

        # Check if credentials match
        if entry_email == self.email and entry_password == self.password:
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")


# Child class 1 (inherits from User)
class Admin(User):
    def __init__(self, name, email, password, account, admin_level, department):
        # Call parent constructor
        super().__init__(name, email, password, account)
        
        # Child-specific attributes
        self.admin_level = admin_level
        self.department = department

    # Method specific to Admin
    def manage_users(self):
        print(f"{self.name} is managing users in {self.department} department.")


# Child class 2 (inherits from User)
class Customer(User):
    def __init__(self, name, email, password, account, address, phone):
        # Call parent constructor
        super().__init__(name, email, password, account)
        
        # Child-specific attributes
        self.address = address
        self.phone = phone

    # Method specific to Customer
    def view_profile(self):
        print(f"Customer: {self.name}, Address: {self.address}, Phone: {self.phone}")


# Create instances of each class
admin_user = Admin("Alice", "alice@email.com", "admin123", 1, "Super", "IT")
customer_user = Customer("Bob", "bob@email.com", "cust123", 2, "Cebu City", "09123456789")

# Test methods
admin_user.login()
admin_user.manage_users()

customer_user.login()
customer_user.view_profile()