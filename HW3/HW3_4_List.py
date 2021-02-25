import functools

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
# 21. Sort lst_to_sort from max to min
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort), "\n", sorted(lst_to_sort, reverse=True))

lst_to_sort_multilpy = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort_multilpy)

# 23*. Raise each list number to the corresponding numbexr on another list:

list_A = [2, 3, 4]
list_B = [5, 6, 7]
new_list = list(map(lambda x, y: y if x < y else y, list_A, list_B))
print(new_list)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
compute_the_number = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(compute_the_number)

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
flt_list = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(flt_list)

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

neg_numbers = list(filter(lambda x: x < 0, range(-10, 10)))
print(neg_numbers)

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

common_list_1_2 = list(filter(lambda x: x in list_1, list_2))
print(common_list_1_2)
