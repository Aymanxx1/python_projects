#6-1. Person
person = {"first name": "ayman", "last name": "mohamed", "age": 23, "city": "cairo"}
print(person["first name"])
print(person["last name"])
print(person["age"])
print(person["city"])

print()
#6-2. Favorite Numbers
favourite_numbers = {
    "ayman": 5,
    "ahmed": 10,
    "medhat": 9,
    "mohamed": 22,
    "khalad": 17,
     }
print(f"ayman's favourite number is {favourite_numbers['ayman']}")
print(f"ahmed's favourite number is {favourite_numbers['ahmed']}")
print(f"medhat's favourite number is {favourite_numbers['medhat']}")
print(f"mohamed's favourite number is {favourite_numbers['mohamed']}")
print(f"khalad's favourite number is {favourite_numbers['khalad']}")

print()
#favourite numbers with loop 6-4
favourite_numbers = {
    "ayman": 5,
    "ahmed": 10,
    "medhat": 9,
    "mohamed": 22,
    "khalad": 17,
     }
for name, value in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is {value} .")
print()
favourite_numbers["emam"]= 20
favourite_numbers["sobhy"]= 11
for name, value in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is {value} .")

print()
#rivers 6-5
rivers = {
    "nile": "egypt",
    "farat": "iraq",
    "messasabe": "england",
     }
for river, country in rivers.items():
    print(f"THe {river.title()} runs through {country.title()}")
print()
for river in rivers.keys():
    print(river)    
print()
for country in rivers.values():
    print(country)

print
#polling 6-6 
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
names = ["jen", "ayman","phil"]
for name in names:
    if name in favorite_languages.keys():
        print(f"{name}, thanks for taking the poll")
    else:
        print(f"{name}, you have to take the poll")
print()
