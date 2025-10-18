hash_map = {}

# Insert key-value
hash_map["roll_no"] = 101
hash_map["name"] = "Sandeep"

# Access value by key
print(hash_map["roll_no"])  # Output: 101

# Update value
hash_map["roll_no"] = 102

# Delete key-value
del hash_map["name"]

print(hash_map)  # Output: {'roll_no': 102}
