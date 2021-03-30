import dataclasses
import collections


class Laptop:
    def __init__(self):
        # laptop_battery = Battery
        self.battery = Battery


class Battery:
    def __init__(self, battery):
        self.battery = battery


laptop = Laptop()


# 2.
class Guitar:
    def __init__(self, guitar_string, guitar_type):
        self.guitar_string = guitar_string
        self.guitar_type = guitar_type


class GuitarString:
    def __init__(self, string_type):
        self.string_type = string_type


guitar_string = GuitarString('steel')
guitar = Guitar(guitar_string, 'electric guitar')


# 3
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should not take instance as first parameter.
#     """


class Calc:

    @staticmethod
    def add_nums(param1, param2, param3):
        return param1 + param2 + param3


print(Calc.add_nums(2, 8, 45))


# 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """

class Pasta:
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])

    def __str__(self):
        return self.list_of_ingredients


pasta1 = Pasta(["tomato", "cucumber"])
print(pasta1.list_of_ingredients)
pasta2 = Pasta.bolognaise()
print(pasta2.list_of_ingredients)


# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


concert = Concert()
Concert.max_visitors_num = 50
concert.visitors_count = 1000
print(concert.visitors_count)


# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
#     birthday (str), age (int)
#     """
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: str


address_book = AddressBookDataClass(1, 'Vitalii', '0681111111', 'Sumska 1', 'v@gmail.com', '18.09.00', '30')
print(address_book)

# 7. Create the same class (6) but using NamedTuple

AddressBookDataClass = collections.namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address',
                                                                       'email', 'birthday', 'age'])


# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     """

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"(key: {self.key}, name: {self.name}, phone_number: {self.phone_number}, address: {self.address}," \
               f"email: {self.email}, birthday: {self.birthday}, age: {self.age} )"


# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    name = "Jonh"
    age = 36
    country = "USA"


person = Person()
setattr(person, "age", 30)
print(getattr(person, "age"))


# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(7, "Petr")
setattr(student, 'student_email', 'v@gmail.com')
print(getattr(student, 'student_email'))


# 11*.
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)
class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    # getting the values
    @property
    def temperature(self):
        print('Getting value')
        return (self._temperature * 1.8) + 32

x = Celsius(10)
print(f'Temperature by Celcius {x._temperature} by Fahrenheit {x.temperature}')