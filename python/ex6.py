# variable descirbing the "types_of_people" 
types_of_people = 10
# another way to write strings in python use the "f"
x = f"There are {types_of_people} types of people."
# a vairbale for the word binary 
binary = "binary"
# a variable for the word "do_not"
do_not = "don't"
# a string variable with the f 
y = f"Those who know {binary} and those who {do_not}."

# print out the variable x
print(x)

# print out the variable y 
print(y)

# print the stirng 
print(f"I said: {x}")
# print the string with the y varibale 
print(f"I also said: '{y}'")

# a vairble named "hilarious "
hilarious = False

# a variable names "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! {}"

# printing the two vairbales listed above with a .format for hilarious 
print(joke_evaluation.format(hilarious))
# variables for w nad e
w='This is the left side of....'
e= "a string with a right side."
# print the two variables togther 
print(w + e)