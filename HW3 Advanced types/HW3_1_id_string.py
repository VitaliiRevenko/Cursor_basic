# 1. Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(f"int_a = {id(int_a)}"
      f"\n str_b = {id(str_b)}"
      f"\n set_c = {id(set_c)}"
      f"\n lst_d = {id(lst_d)}"
      f"\n dict_e = {id(dict_e)}")
#################################################
# 2. Append 4 and 5 to the lst_d and define the id one mor
lst_d.append(4)
lst_d.append(5)
print(f"lst_d = {id(lst_d)}")
#################################################
# 3. Define the type of each object from step 1.
for lst in lst_d:
    print(type(lst))
# 4*. Check the type of the objects by using isinstance.
for lst in lst_d:
    print(isinstance((lst), int))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
#
# 5. With .format and curly braces {}

print("Anna has {apples}  apples and {peaches} peaches.".format(apples=5, peaches=10))

# 6. By passing index numbers into the curly braces.

print("Anna has {0}  apples and {1} peaches.".format(5, 10))

# 7. By using keyword arguments into the curly braces.

print("Anna has {}  apples and {} peaches.".format(5, 10))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:^4}  apples and {1:^2} peaches.".format(5, 10))

# 9. With f-strings and variables

apples = 5
peaches = 10
print(f"Anna has {apples}  apples and {peaches} peaches.")

# 10. With % operator
print("Anna has %s  apples and %s peaches." % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)

data_dict = {"number_of_apples": apples, "number_of_peaches": peaches}
print("Anna has %(number_of_apples)s  apples and %(number_of_peaches)s peaches." % data_dict)