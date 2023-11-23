from sys import argv 
script , user_name = argv 
prompt ='> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f""" 
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")


print(f"""{user_name}, I know you like me but I'm a little older 
      for us to continue this relationship I need to know your age
      """)

print("Enter your age?")
age = input(prompt)


print(f"""
 Sorry!!! {user_name},you are {age} years old , I need an older  man you are too young for me :(
 """)