''' create and setup a user '''

# imports
import os
import json

class User():
    def __init__(self):
        pass
    # name
    def name(self):
        fname = str(input("enter your first name: "))
        lname = str(input("enter your last name: "))
        name = { "fname": fname, "lname": lname }
        return name
    
    # class logs are being used for
    def class_name(self):
        class_name = str(input("enter name of class log is being used for: "))
        return class_name

    # email (validate)
    def email(self):
        email_requirements = ["@","."]
        email = str(input("enter your email: (me@me.com)"))
        for req in email_requirements:
            while req not in email:
                print("email invalid; missing: ", email_requirements)
                email = str(input("retry entering an email: (me@me.com) "))
            else:
                print("email valid!")
                break
        return email

    # build the user
    def build_user(self):
        user = { 
        "name": User().name(), 
        "class": User().class_name(),
        "email": User().email(),
        }
        return user

    def user_to_json(self, user):
        with open("user.json", "w") as file:
            print("writing user data to json file.")
            json.dump(user, file, indent=4)
        print("complete")

if __name__ == "__main__":
    user = User().build_user()
    user_to_json = User().user_to_json(user)
