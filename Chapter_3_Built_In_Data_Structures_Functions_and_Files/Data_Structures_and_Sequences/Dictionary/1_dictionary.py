empty_dict = {}

d1 = {"a": "some value", "b": [1,2,3,4] }

print(d1)

# You can access, insert, or select elements using the same syntax as for accessing elements of a list or tuple

d1[7] = "an integer"
print(d1)

print(d1["b"])

# Check if contains a specific value

print("b" in d1)

list_keys = list(d1.keys())
print(list_keys)

list_values = list(d1.values())
print(list_values)

# In order to iterate over the keys and values, you can use the items method to iterate over the keys values as 2-tuples:

list_items = list(d1.items())
print(list_items)