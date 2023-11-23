# variable for cars pass the value "100"
cars = 100
# if you remove 4.0 and put 4 it just because an integer 
space_in_a_car = 4
# Variable for drivers pass the value "30"
drivers = 30
# Variable for passengers pass the value "90"
passengers = 90
# Variable for cars_not_driven subtract cars from drivers 
cars_not_driven = cars - drivers 
# Variable for cars_driven is equal to drivers 
cars_driven = drivers 
# Variable for carspool_capacity  is cars_driven mutliplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Variable for average_passengers_per_car  is passengers diveided by cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are ",cars,"cars available.")
print("There are only", drivers,"drivers available.")
print("There will be ", cars_not_driven,' empty cars today')
print("We can transport ", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about ", average_passengers_per_car, "in each car.")
