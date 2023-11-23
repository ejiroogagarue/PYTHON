from sys import argv
# read the WYSS section for how to run this 
age= input("How old are you?")
script , first , second , third = argv

print("The script is called", script)
print("your first variable is:",first)
print("Your second variable is:",second)
print("Your second variable is:",third)
print(f"You are {age} years.")
