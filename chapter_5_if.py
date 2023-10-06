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
if age >18 :
    print(True)
####
age = 11
if age <= 15:
    print(True)
####
age_0 = 15
age_1 = 20
if (age_0>=20) and (age_1>=20):
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
