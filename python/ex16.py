# Import the module argv for usage 
from sys import argv 

# we will capture the script and filename we want to use 
script, filename = argv 

# print the name of the file 
print(f"We're going to erase {filename}.")

# print the command ctrlc to stop the process 
print("If you don't want that , hit CTRL-C (^C).")

# print return or enter to continue 
print("If you do want that, hit RETURN. ")
input("?")


# Prompt indicating the file is being opened 
print("Opening the file...")

# variable to open the file 
target = open(filename, 'w')


# print the prompt "Truncating the file. Goodbye!"
print("Truncating the file. Goodbye!")

# truncating the file what does this do 
target.truncate()

print("Now I'm going to ask you for three lines.")
# input text 
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to wrtie these to the file.")
 # pass the input text varaibles and write them into the file 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# always close a file this similiar to saving 
print("And finally, we close it.")
target.close()