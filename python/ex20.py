from sys import argv

# pass the argv module property to the two variables
script, input_file = argv

# function print_all which print the read file details 
def print_all(f):
    print(f.read())

# function rewind it containes a seek function 
# seek() function is used to change the position of the File Handle to a given specific position
def rewind(f): 
    f.seek(0)

# function that has two argments line_count and f
def print_a_line(line_count, f):
    # print the line_count
    # The readline() method returns one line from the file.
    # print line count and the text on the line 
    print(line_count, f.readline())

# variable to open the "input_file"
current_file = open(input_file)

# print the text "First lets print the whole file "newline" "
print("First lets print the whole file:\n")

# print the the files details 
print_all(current_file)

# print the string " Now lets rewind, kind of like a tape."
print("Now lets rewind, kind of like a tape.")

# pass the currentfile to the function rewind 
rewind(current_file)

# print the string "Lets print the three lines:"
print("Lets print three lines:")

# pass the value "1" to the current_file variable
current_line = 1
print_a_line(current_line, current_file)

# pass the value "1" to the current_file variable
current_line +=  1
print_a_line(current_line, current_file)

# pass the value "1" to the current_file variableq

current_line += 1
print_a_line(current_line, current_file)