# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Sydney'
}

# info = ['Alice', 25, 'Sydney'] # Above dictionary is more structured

# Access the values by keys
print(my_dict['city'])
print(my_dict['age'])

# Adding a new key-pair value
my_dict['email'] = 'alice@exmaple.com'
print(my_dict)

# Adding an item with an existing key overwrites the original value
my_dict['city'] = 'Melbourne'
print(my_dict)

# Removing a key-value pair
del my_dict['age']
print("----------")
print(my_dict)

# Alternatively, you can use .pop ()
my_dict.pop('email')
print(my_dict)

# Checking for key existence
print("----------")
print('email' in my_dict)
print('name' in my_dict)

# Interate through dictionary
for key, value in my_dict.items():
    print(f"{key}, {value}")

# Nested dictionaries
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}

print(nested_dict['person2']['name'])

# Merging dictionaries
merged_dict = my_dict | nested_dict
print(merged_dict)