# Strings
#    data that falls within " " marks

# concatenation
# put 2 or more strings together

firstName = "Fred"
lastName = "Flintstone"

print(firstName + " " + lastName)

fullName = firstName + " " + lastName


print(fullName)

# repitition
#  Repitition operator: *

print("Hip"*2 + "Hooray!")
def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")
    print("dream, "*5)

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])
print(name[-2])
