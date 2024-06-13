# Creating a set
my_set = {1, 2, 3, 4, "Apple"}

print(my_set)

# Adding an element
my_set.add(5)
print(my_set)

# Removing an element
my_set.remove(2)
print(my_set)

# Membership testing
print(2 in my_set)
print(3 in my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_value = set_a.union(set_b)
print(union_value)

# Intersection
intersection_value = set_a.intersection(set_b)
print(intersection_value)

# Difference - set_a values minus intersection value
difference_value = set_a.difference(set_b)
print(difference_value)
# Difference - set_b values minus intersection value
difference_value = set_b.difference(set_a)
print(difference_value)

