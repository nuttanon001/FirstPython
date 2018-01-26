# String list
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')

# Number list
digits = [1,2,3,4,5,6,7,8,9,0]
print('Min:',min(digits))
print('Max:',max(digits))
print('Sum:',sum(digits))

# Copy List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Input
age = input("How old are you?\n")
print('Your age is',str(age))

# Arbitrary send parm don't know
# Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')