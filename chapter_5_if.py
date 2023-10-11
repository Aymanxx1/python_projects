#chapter_5 
#more conditional tests 5-2
car = "bwm"
if car == "bwm":
    print(True)
if car != "bwm":
    print(True)
#######
name = "Ayman"
name =name.lower()
if name == "ayman":
    print(name)
####
age = 23
if age > 18 :
    print(True)
####
age = 11
if age <= 15:
    print(True)
####
age_0 = 15
age_1 = 20
if (age_0 >= 20) and (age_1 >= 20):
    print(True)
###
number = 300
number_2 = 100
if number == 300 or number_2 == 1000:
    print(True)
####
cars = ["bmw", "toyta"]
if "bmw" in cars :
    print("used")
if "honda" not in cars :
    print("not in the list")
print()
#Alien colors 5-3
alian_color = "red"
if alian_color == "green":
    print("you just earned 5 points")
if alian_color == "red":
    print("you just earned 10 points")

print()
#Alien colors 5-4
if alian_color == "green":
    print("you earned 5 points")
else:
    print("you earned 10 points")

print()
#Alien colors 5-5
if alian_color == "grean":
    print("you earn 5 points")
elif alian_color == "yellow":
    print("you earn 10 points")
else :
    print("you earn 15 points")

print()
#stages of life 5-6
age = 23
if age < 2:
    print("you are a baby")
elif age < 4:
    print("you are a toddler")
elif age < 13:
    print("you are a kid")
elif age < 20:
    print("you are a teenager")
elif age < 65:
    print("you are a adult")
else:
    print("you are an elder")

print()
#favourite_fruits 5-7
favourite_fruits = ["banana", "apple", "kewi", "mango"]
if "mango" in favourite_fruits:
    print("i like mango")
if "banana" in favourite_fruits:
    print("i like banana")
if "kwie" in favourite_fruits:
    print("i like kwie")
if "apple" in favourite_fruits:
    print("i like apple")
print()
#Hello Admin 5-8 
names = ["ayman", "mohamed", "khalad", "ramadan", "admin"]
for name in names:
    if name == "admin":
        print(f"Hello {name.title()}, would you like to see a status report?")
    else:
        print(f"Hello, {name.title()}, thank you for logging in again")
print()
#No users 5-9
names = [] 
if names :
    for name in names :
        print("we have some")
else:
    print("we need some users")
print()

#checking usernames 5-10
current_users = ["ayman", "mohamed", "emam", "khalad","ahmed"]
new_users = ["Ayman", "ramadan", "eman", "Khalad","mostafa"]
for user in new_users:
    if user.lower() in current_users:
        print(f"{user.title()}, not avalible you need to enter a new user")
    else:
        print(f"{user.title()}, your user is avalible")

print()
#ordinal numbers 5-11
numbers = list(range(1,10))
for number in numbers:
 if number == 1:
     print(f"{number}st")
 elif number == 2:
     print(f"{number}nd")
 elif number == 3:
     print(f"{number}rd")
 else:
    print(f"{number}th")