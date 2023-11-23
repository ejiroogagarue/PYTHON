#We have three variables people, cars and trucks 
people = 30 
cars = 40
trucks = 15

# if statment for "cars > people"
if cars > people:
    # print the string "We should take the cars."
    print("We should take the cars.")

# elif statement for "cars < people"
elif cars < people:
    # print the string "We should not take the cars."
    print("We should not take the cars.")
# else statement for if none of the if or elif work 
else: 
    # print the statement "We can't decide."
    print("We can't decide.")

# a thing to note this is a new set 
# if trucks > cars 
if trucks > cars:
    # print "That's too many trucks."
    print("That's too many trucks.")
# else if "trucks < cars"
elif trucks < cars:
    # print maybe we could take the trucks.
    print("Maybe we could take the trucks.")
else: 
    # else "We still can't decide"
    print("We still can't decide.")

if people > trucks:
    print("Alright, lets just take the trucks.")
else: 
    print("Fine, lets stay home then.")