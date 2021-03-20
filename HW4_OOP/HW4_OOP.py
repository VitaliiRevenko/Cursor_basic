# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have
# seating_capacity own method
class Bus(Vehicle):
    def seating_capacity(self, seat):
        self.seat = seat


# 3. Determine which class a given Bus object belongs to (Check type of an object)
school_bus = Bus(100, 200)
print(f"Bus class belongs to {school_bus.__class__} ")
print(f"Max speed = {school_bus.max_speed} and mileage {school_bus.mileage}")

# 4. Determine if School_bus is also an instance of the Vehicle class
print(f"Is school_bus an instance of the Vehicle class?:\t", isinstance(school_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own
# - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, bus_school_color):
        School.__init__(self)
        Bus.__init__(self)
        self.bus_school_color = bus_school_color


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
class Bear():
    def make_sound(self):
        print(f"I'm a bear and I make sound Bearrrrrrrr:")


class Wolf():
    def make_sound(self):
        print(f"I'm a wolf and I make sound Wolfffff:")


bear = Bear()
wolf = Wolf()
animals_sound = (bear, wolf)
[anm_snd.make_sound() for anm_snd in animals_sound]


# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        new_instance = super(City, cls).__new__(cls)
        if population > 1500:
            return new_instance
        else:
            print("Your city is too small")

    # 9. Override a printable string representation of the City class and return: The population of the city
    # {name} is {population}
    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater
# than 10. And perform this add (+) of two instances.
class Add:
    def __init__(self, number):
        self.number = number

    def __add__(self, other_number):
        if self.number > 10 or other_number.number > 10:
            result = self.number * other_number.number
        else:
            result = other_number.number + self.number
        return Add(result)

    def __str__(self):
        return f"{self.number}"

    def __repr__(self):
        return f"{self.number}"


num_1, num_2 = Add(5), Add(9)
result_1 = num_1 + num_2
print(result_1)
num_3, num_4 = Add(11), Add(9)
result_2 = num_3 + num_4
print(result_2)


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions
# and can be called like a function. Create a new class with __call__ method and define this call to return sum.

class Call:

    def __call__(self, a, b):
        return a + b


summa = Call()
print(summa(10, 8))


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        return len(self.cart) != 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(f'Order_1 = {bool(order_1)}\n'
      f'Order_2 = {bool(order_2)}')


