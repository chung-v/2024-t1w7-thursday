#Creating a tuple
my_tuple = (1, 2, 3, 'a', 'happy')

# Accessing elements
print(my_tuple[3])
print(my_tuple[0])

# Attempting to change an element (will raise an error)
# my_tuple[0] = 10 # TypeError: 'tuple' object does not support item assignment

# Tuples can be unpacked
# a = my_tuple[0]
# a = my_tuple[1]
# a = my_tuple[2]
# a = my_tuple[3]
# a = my_tuple[4]
# a = my_tuple[5]
a, b, c, d, e = my_tuple
print(a, e)

# Tuples can contain other tuples (nested tuples)
nested_tuple = (1, (2, 3), (4, 5), (0, 0))
print(nested_tuple[1][1])