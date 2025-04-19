"""How to Open, Read, & Write to Files using the 'with' Keyword"""

#TODO-1: Involves manually Closing the opened file.
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close() #closes the opened files to free up the computer spaces

#TODO-2: Using 'with' keyword --> Automatically closes down the file opened ******
"""Involves only 'READING' the file --> mode set to READ-only (mode="r")"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#TODO-3: To perform both 'READING & WRITING,' the file --> mode set to Write (mode="w")
with open("my_file.txt" , mode="w") as file:
    file.write("New Text.")
#it rewrites the files, deleting the previous saved texts in the file

#TODO-4: To perform both 'READING & WRITING' the file w/o deleting the previous set of data --> mode set to Append (mode="a")
with open("my_file.txt" , mode="a") as file:
    file.write("\nNew text")

#TODO-5: Python can automatically create a new file. But it works only with Write mode --> (mode="w")
with open("new_file.txt" , mode="w") as file:
    file.write("Hey it's Aryan Jaiswal")