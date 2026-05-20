# Dictionaries
band = {
    "Vocals" : "Plant",
    "Guitar" : "Page"
}

band2 = dict(Vocals= "Plant", Guitar = "page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Accessing items
print(band["Vocals"])
print(band.get("Guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# Verify a key exists
print("Guitar" in band)
print("triangle" in band)

# Change values
band["Vocals"] = "Coverdale"
band.update({"Bass": "JPJ"})

print(band)

# Removing items
print("")
print(band.pop("Bass"))
print(band)

band["Drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete and clear item
print("")
band["Drums"] = "Bonham"
del band["Drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# band2 = band    #Create a reference
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["Drums"] = "Dave"
# print(band)                         # Bad way to copy

band2 = band.copy()
band2["Drums"] = "Dave"
print("Good Copy!")
print(band)
print(band2)

# Or use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)

print("")
# Nested Dictionaries
member1 = {
    "name": "Plant",
    "instrument": "Vocals"
}
member2 = {
    "name": "Page",
    "instrument": "Guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])
