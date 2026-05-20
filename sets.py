nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)         # It prints only one of the 2s and ignore the other one

# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# But you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)

# You can use .update with lists, tuples, and dictionaries

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

my_new_set = one.union(two)
print(my_new_set)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
