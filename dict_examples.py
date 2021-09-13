# Dictionary Examples

# A dictionary is a pythonic data structure that uses key-value pairs

# Syntax for a dictionary is 
# {'key': 'value'}

# A key must be a string, or a variable that resolves to a string

# A value may be any valid pythonic type, including: str, int, float, list, dict and more!

# A blank dictionary of pets
pets = {}

# one way to add or update existing key-value pairs to a dictionary
pets.update({"dogs": ["toto"]})
print(pets)
# > {"dogs": ["toto"]}

# another way to add or update existing key-value pairs to a dictionary (preferred)
pets["cats"] = ["fluffy", "snowball", "garfield"]
print(pets)
# > {"dogs": ["toto"], "cats": ["fluffy", "snowball", "garfield"]}

# Updating dogs
pets["dogs"] = ["toto", "spot", "kujo"]
print(pets)
# > {"dogs": ["toto", "spot", "kujo"], "cats": ["fluffy", "snowball", "garfield"]}

# Add a single fish
pets["fish"] = "dorothy"
print(pets)
# > {"dogs": ["toto", "spot", "kujo"], "cats": ["fluffy", "snowball", "garfield"], "fish": "dorothy"}

# In order to access values within a dictionary, you use the key
# Think of this like looking up the keyword ROFL on urbandictionary.com - you then get a value returned
print(pets["dogs"])
# > ["toto", "spot", "kujo"]

print(pets["cats"])
# >  ["fluffy", "snowball", "garfield"]

print(pets["fish"])
# > "dorothy"

# To dive into a data structure within a data structure (list in a dictionary), just keep putting more square brackets next to each other
print(pets["dogs"][0])
# > "toto"
print(pets["dogs"][1])
# > "spot"
print(pets["dogs"][2])
# > "kujo"

print(pets["fish"][:3]) # string slicing is just like list slicing! Get the first 3 characters of the string 
# > "dor"



