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











