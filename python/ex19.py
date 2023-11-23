# function called cheese_and_crackers with arguments cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print strings with the arguments passed in this case "You have {cheese_count} cheeses"
    print(f"You have {cheese_count} cheeses!")
    # print string with the arguments passed --> in this case "You have {boxes_of_crackers} boxes of crackers"
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print the string "Man that's enough for a party!"
    print("Man that's enough for a party!")
    # pirin the string "Get a blanket newline"
    print("Get a blanket. \n")

# print "We can just give the function numbers directly"
print("We can just give the function numbers directly:")

# run the cheese and crackers function with the values (20 , 30)
cheese_and_crackers(20, 30)

# print the string "OR, we can use varaibles from our script"
print("OR, we can use variables from our script:")

# variable with the name "amounbt_of_cheese" pass the value ---> 10
amount_of_cheese = 10
# Varibale with the name "amount_of_crackers" pass the value ---> 50
amount_of_crackers = 50


# run the function cheese_and_crackers with the variables "amount_of_cheese and the "amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print the string "We can do math inside too:"
print("We can even do math inside too:")
# run the function cheese_and_crackers witht valuers "10+20" and "5+6"
cheese_and_crackers(10+ 20, 5+6)

print("And we can combine the two, varaibles and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


