# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

# 12. Convert (1) to list comprehension
convert_1_to_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(convert_1_to_comprehension)

# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

# 13. Convert (2) to regular for with if-else

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
##############################################################################
# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
##################################################################################

# 14. Convert (3) to dict comprehension.
d_comprehension1 = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(d_comprehension1)

# 15*. Convert (4) to dict comprehension.
d_comprehension2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comprehension2)
# 16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)
# 17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)
