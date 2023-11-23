import sys 
script, filename = sys.argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()

print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")



txt = open('ex15_sample.txt')

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt.read())


print('Let\'s practice everything.')
print("""You\'d need to know \'bout escapes 
      with  that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 
print(f"This should be five: {five}")

def secret_formula(beans, jars):
    jelly_beans = beans * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

beans = 10
jars = 50
crates = 250
start_point = 10000
formula = secret_formula(beans, jars)

# remember that this is another way to format a string
print("With a starting point of: {}".format(formula))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(beans, jars)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
