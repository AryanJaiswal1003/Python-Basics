class User:
    pass
"""The pass statement is used during development phase when you are planning the structure of your code 
    but haven't implemented all details yet. It helps to avoid syntax errors and keeps your code running smoothly."""

user_1 = User()

"""PascalCase = Naming convention in which first letter of each word in a compound word is capitalized, & no spaces 
    or underscores are used between words"""

"""camelCase = Style of writing where each word in middle of a phrase is written with a capital latter, & no space or 
    underscore are used between words"""

"""snake_case = Naming convention where words are written in lowercase & separated by underscores"""

#TODO-Theory: Working with Attributes, Class Constructors and the __init__() Function: -

"""Attribute = it is a variable that is associated with a variable --> adding '.' notation after the object --> here the 
object is user_2"""

class UserName:
    pass

user_2 = UserName()
user_2.id = "001"
user_2.username = "Aryan Jaiswal"

print(user_2.username)

"""Constructor = part of the blueprint that allows us to specify what should happen when our object is constructed i.e.
'Initializing' an object i.e. we can set the variables or counters to the starting value"""

#Constructor in Python is created by '__init__(self , parameters)' function

class Toffee:
    def __init__(self , name , user_id):
        self.name = name
        self.user_id = user_id
        self.quantity = 0

toffee_1 = Toffee("Kinder_Joy" , "001")
toffee_2 = Toffee("Melody" , "002")

print(toffee_1.name , "-->", toffee_1.user_id)
print(f"Quantity -->" , toffee_1.quantity)