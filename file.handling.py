#File handling is an important part of any web application.
#Python has several functions for creating, reading, updating, and deleting files.

#File Handling
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
"""
#There are four different methods (modes) for opening a file:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#open the file "demofile3.txt" and overwrite the content:

f=open("demofile3.txt","w")
f.write("Woops,I have deleted the content!")
f.close()

#open and read the file after the overwriting:

f=open("demofile3.txt","r")
print(f.read())

