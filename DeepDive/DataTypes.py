import sys

# Integers
int_size = sys.getsizeof(42)

# Floats
float_size = sys.getsizeof(3.14)

# Strings
string_size = sys.getsizeof("Hello, World!")

# Lists
empty_list_size = sys.getsizeof([])
non_empty_list_size = sys.getsizeof(["va"])

# Tuples
empty_tuple_size = sys.getsizeof(())
non_empty_tuple_size = sys.getsizeof((1, 2, 3))

# Dictionaries
empty_dict_size = sys.getsizeof({})
non_empty_dict_size = sys.getsizeof({'a': 1, 'b': 2, 'c': 3})

print(f"Size of int: {int_size} bytes")
print(f"Size of float: {float_size} bytes")
print(f"Size of string: {string_size} bytes")
print(f"Size of empty list: {empty_list_size} bytes")
print(f"Size of non-empty list: {non_empty_list_size} bytes")
print(f"Size of empty tuple: {empty_tuple_size} bytes")
print(f"Size of non-empty tuple: {non_empty_tuple_size} bytes")
print(f"Size of empty dictionary: {empty_dict_size} bytes")
print(f"Size of non-empty dictionary: {non_empty_dict_size} bytes")
