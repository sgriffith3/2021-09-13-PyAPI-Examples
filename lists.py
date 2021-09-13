# Pythonic List Examples

# blank list called pets
pets = []

# add a "cat" to the list of pets
pets.append("cat")
print(pets)
# > ["cat"]

# add a "dog" to the list of pets
pets.append("dog")
print(pets)
# > ["cat", "dog"]

# Note that the methond append means 'add to the end'

# add a "fish" to the list of pets
pets.append("fish")
print(pets)
# > ["cat", "dog", "fish"]

# You can now access items in a list by their index number

#         ["cat", "dog", "fish"]
#  index     0      1      2

print(pets[0])  # "cat"
print(pets[1])  # "dog"
print(pets[2])  # "fish"

# There also are negative indexes
# But there is no negative zero, so start at negative 1

#           ["cat", "dog", "fish"]
#  index       0      1      2
#  neg index  -3     -2     -1

print(pets[-3])  # "cat"
print(pets[-2])  # "dog"
print(pets[-1])  # "fish"

# Another important aspect of using lists is understanding list slices
# A slice is essentially a piece of a list

print(pets[0:2])
# > ["cat", "dog"]

# slice syntax of listname[<start index>: <stop index>]
#             pets[0:2]
# This can be read "Take the list called pets, start with item at index 0 up to but not including item at index 2"

# A slice that has a colon will always return a list. Just accessing a single index will return the item itself

print(pets[1:])
# > ["dog", "fish"]
# "Take the list called pets, start with the item at index 1 until the end of the list"

print(pets[::2])
# > ["cat", "fish"]
# "Take the list called pets, start with the item at the first index, go until the end of the list, but step 2 indexes each time
# full list slicing syntax is:
# listname[<start index>: <stop index>: <step number of indexes>]
# So this last example had us start at index 0, and then step up to the item at index 2


# Another example
sports_cars = ["ferrari", "bugatti", "koenigsegg"]

trucks = ["F150", "Sierra", "Tacoma"]

vehicles = sports_cars + trucks
print(vehicles)
# ["ferrari", "bugatti", "koenigsegg", "F150", "Sierra", "Tacoma"]











