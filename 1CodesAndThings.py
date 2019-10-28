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


for i in range(len(name)):
    print(name[i])

# slicing and Dicing
#   Slicing Operator:  :
#   slicing lets us make substrings

print(name[0:5])
print(name[0:6])
print(name[:5])
print(name[6:9])
print(name[6:])



# Searching inside of Strings

print("Biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in name")
else:
    print("the letter y in not in name")


# Character functions

print(ord('5'))

print(chr(97+13))

print(str(12458))