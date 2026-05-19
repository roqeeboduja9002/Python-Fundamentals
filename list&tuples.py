users = ["Dave", "John", "Sara"]

print("Dave" in users)

print(users[0])
print(users[-1])        # Last value
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[0:])

print(len(users))

users.append("Elsa")
print(users)

users += ["Jason"]      # 1st Method
print(users)

users.extend(["Robert", "Jimmy"])       #2nd Method
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ("Eddie", "Alex")
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)


users.remove("Bob")
print(users)

users.pop()
print(users)

# del users[0]
# users.clear()
# print(users)

users[1:2] = ["dave"]
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))

nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(nums_copy)
print(my_nums)
my_copy.sort()
print(my_copy)
print(nums)

print(type(nums))

my_list = list([1, "Neil", True])
print(my_list)

# Tuples
my_tuple = tuple(("Dave", 42, True))

another_tuple = (1, 4, 2, 7, 2, 2)

print(my_tuple)
print(type(my_tuple))
print(type(another_tuple))

# Tuples can"t be changed
new_list = list(my_tuple)
new_list.append("Neil")
new_tuple = tuple(new_list)
print(new_tuple)

print(another_tuple.count(2))
