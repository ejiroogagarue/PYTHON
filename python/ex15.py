# import the argv module into your script
from sys import argv

# pass the arguments script and filename for the arguments 
script, filename = argv


# variable "txt" open the file 
txt = open(filename)

# print "Here your file the file we opened"
print(f"Here's your file {filename}:")

# print out the content of the text file 
print(txt.read())

# a prompt to type the file again 
print("Type the filename again:")

# input variable to insert the file name 
file_again = input("> ")

# opens the file 
txt_again = open(file_again)
file_again.close()

# prints the content of the file.
print(txt_again.read())
txt_again.close()

