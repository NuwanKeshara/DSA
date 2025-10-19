
# a = ["a", 2]
# b = ["a", 2]

# if a == b:
#     print('yes')
# else:
#     print("no")


# immutable object
a = b = 0

# mutable object
a = b = {}

print(id(a))
print(id(b))

a[1] = 1

print(id(a))
print(id(b))

