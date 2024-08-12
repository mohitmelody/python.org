#   about static method
#  class  aur use method ko access karne ke liye Mujhe Uska Ek object variable banana paratha hai
#  par agar mujhe uske bina access so it possible by static method
# Define a class named 'newskills'
class newskills:
    # Constructor method to initialize phone number and email ID
    def __init__(self, phonemunber, email_id):
        self.phone_number = phonemunber
        self.email_id = email_id

    # Static method that prints a list of gods
    @staticmethod
    def staticControl(list_of_gods):
        return print(list_of_gods)

# Example usage of the static method without creating an object
# newskills.staticControl("[God 1 , God 2 , God 3]")

# Case 2: Using a static method inside a class method and accessing it with an object variable
class newskills:
    def __init__(self, phonemunber, email_id):
        self.phone_number = phonemunber
        self.email_id = email_id

    @staticmethod
    def staticControl(list_of_gods):
        return print(list_of_gods)

    @classmethod
    def fetchStaticcontrol(cls):
        cls.staticControl("[ happ1 , haap2 , haap3]")

# Example usage of the static method and class method
# newskills.staticControl("[God 1 , God 2 , God 3]")
# newskills.fetchStaticcontrol()

# Case 3: Calling one static method from another static method
class newskills:
    def __init__(self, phonemunber, email_id):
        self.phone_number = phonemunber
        self.email_id = email_id

    @staticmethod
    def staticControl2(list_of_gods):
        return print(list_of_gods)

    @staticmethod
    def staticControl(list_of_gods):
        # Calling another static method within a static method
        newskills.staticControl2(["yellow , green mango"])
        return print(list_of_gods)

    @classmethod
    def fetchStaticcontrol(cls):
        cls.staticControl("[ happ1 , haap2 , haap3]")

# Example usage of the static methods and class method
# newskills.staticControl("[God 1 , God 2 , God 3]")
# newskills.fetchStaticcontrol()
# newskills.staticControl("[God 1 , God 2 , God 3]")

# Case 4: Accessing a static method inside an instance method
class newskills:
    def __init__(self, phonemunber, email_id):
        self.phone_number = phonemunber
        self.email_id = email_id

    # Instance method that calls a static method
    def staticacess(self):
        self.staticControl2(["happy1" , "happ2 "])

    @staticmethod
    def staticControl2(list_of_gods):
        return print(list_of_gods)

    @staticmethod
    def staticControl(list_of_gods):
        newskills.staticControl2(["yellow , green mango"])
        return print(list_of_gods)

    @classmethod
    def fetchStaticcontrol(cls):
        cls.staticControl("[ happ1 , haap2 , haap3]")

# Example usage of the instance method that calls a static method
obj1 = newskills(894759034, "8943@gmail.com")
obj1.staticacess()
