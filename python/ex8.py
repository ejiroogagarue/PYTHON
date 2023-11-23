#the formatter variable takes three values 
#if you remove "{}" any of these it reduces the number of values 
formatter = "{} {} {} {}"

# pass the formatter variable to different values of different properites 
#Number
print(formatter.format(1,2,3,4))
#String
print(formatter.format("one","two", "three","four"))
#Boolean
print(formatter.format(True, False, False, True))
#the variable 
print(formatter.format(formatter, formatter, formatter, formatter))
# a set of sentences 
print(formatter.format("Try your","Own text here","Maybe a poem","Or a song about fear"))