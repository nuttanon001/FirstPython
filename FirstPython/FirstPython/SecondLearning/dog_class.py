class Dog():
    """description of dog"""

    def __init__(self,name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a gog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """SImulate rolling over in response to a command."""
        print(self.name.title() + "rolled over!")


my_dog = Dog('Dang',5)

print("My dog's name is" , my_dog.name.title() , ".")
print('My dog is', str(my_dog.age) , 'years old.')
# Calling method in class
my_dog.sit()