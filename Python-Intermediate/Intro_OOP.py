"""Object-Oriented Programming (OOP)"""
#attributes = free floating variable that is attached to a particular object (thing which we "have")
#methods = function when tied to an object (things which we have to "do")

"""Using Class(Blueprint/Types) to create an actual Object """
"""Constructing Object"""

"""car [object] = CarBlueprint() [class] --> PascalCase = variable naming convention in 
programming where 1st letter of each word is capitalized, & there are no spaces or underscore separators b/w words."""


"""Link to Turtle = https://docs.python.org/3/library/turtle.html#turtle.color"""

"""Either this way"""

# import turtle
# timmy = turtle.Turtle()

"""Or this way"""

from turtle import Turtle , Screen
timmy = Turtle()
print(timmy) #output = <turtle.Turtle object at 0x00000284656E5400> i.e. a file is saved in computer in this location
timmy.shape("turtle")
timmy.color("coral")
for i in range(100):
    timmy.forward(i)
    timmy.right(50)
    timmy.left(i)


"""Object Attributes"""

my_screen = Screen() #Screen is the window in which the Turtle is going to show up
print(my_screen.canvheight) #here my_screen(object).canvheight(attribute) #Output = 300 i.e. the height of the screen.

"""Object Method"""

my_screen.exitonclick()#my_screen(object).exitonclick(method)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column(fieldname="Pokemon Name" , column=["Pikachu" , "Squirtle" , "Charmander"])
table.add_column(fieldname="Type" , column=["Electric" , "Water" , "Fire"])
table.align = "l"
print(table)

"""Link for PrettyTable = https://pypi.org/project/prettytable/"""