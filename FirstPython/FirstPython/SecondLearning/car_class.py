from json import JSONEncoder,dump,load

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initializ attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descripive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print('This car has',str(self.odometer_reading),'miles on it.')

    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if (mileage >= self.odometer_reading):
            self.odometer_reading = mileage
        else:
            print("Ypu can't roll back an odometer!")

    def increment_odometer(self,miles):
        """Add the give amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 70):
        """Initializ the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print('This car has a',str(self.battery_size),"-kWh battery.")
       
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 255

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self,battery):
        if battery:
            self.battery_size = battery

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery = Battery()):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = battery
        #self.battery_size = 70

    #def describe_battery(self):
    #    """Print a statement describing the battery size."""
    #    print("This car has a " + str(self.battery_size) + "-kWh battery.")

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__ 

def newLine():
    print('-----------------------')

my_new_car = Car('Toyata', 'altis', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
newLine()
my_user_car = Car('Honda','jazz',2009)
print(my_user_car.get_descriptive_name())

my_user_car.update_odometer(192312.5)
my_user_car.read_odometer()

my_user_car.increment_odometer(100)
my_user_car.read_odometer()
newLine()
my_tesla = ElectricCar('tesla' , 'model s' , 2016, Battery(85))
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(23)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery(85)
my_tesla.battery.get_range()



def save_class_to_json():
    # Try to save to Json
    filename = 'car_data.json'
    with open(filename, 'w') as f_obj:
        dump(my_tesla, f_obj,cls=MyEncoder)

from collections import OrderedDict
def load_class_to_json():
    # Try to load to json
    filename = 'car_data.json'

    with open(filename) as f_obj:
        load_tesla = load(f_obj,object_hook = as_electric_car)
        print(load_tesla.get_descriptive_name())
        load_tesla.read_odometer()
        load_tesla.battery.get_range()

def as_electric_car(car):
    if 'make' in car:
        return ElectricCar(car['make'], car['model'], car['year'])
    return None

newLine()
print('Json load data')
load_class_to_json()