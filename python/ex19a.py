def test_function(one, two):
    print(f"i have {one} and {two}")


one = 10 

two = 20

age=input("How old are you?")
height=input("How tall are you?")

ageOne = int(age)
heightOne = int(height)
test_function(two, one)
test_function("hey","baby")
test_function(1+7, 10+90)
test_function("%","$")
test_function(one-two,two-one)
test_function(age, height)
test_function(ageOne+heightOne, heightOne-ageOne)
test_function(f"{age} in years", f"{height} inches")