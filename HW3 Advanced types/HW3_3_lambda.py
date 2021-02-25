# Lambda:

# 18. Convert (7) to lambda function ###########################################
#  (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
foo = lambda x, y: x if x < y else y
print(foo(5, 10))


# 19*. Convert (8) to regular function ###########################################
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(10, 1, 5))
