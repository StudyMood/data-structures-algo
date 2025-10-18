# Create set
hash_set = set()

# Insert
hash_set.add(10)
hash_set.add(20)
hash_set.add(20)  # duplicate, ignore hoga

# Search
print(10 in hash_set)  # Output: True
print(30 in hash_set)  # Output: False

# Delete
hash_set.remove(10)
print(hash_set)        # Output: {20}
# This is hash_set.py
