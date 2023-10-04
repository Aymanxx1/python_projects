#list chapter 
#names 3-1 
names = ["ayman", "mahmoud", "khalad", "sarah"]
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print()
#greetings 3-2 
print(f"{names[0].title()}, How are you doing ?")
print(f"{names[1].title()}, would you like to come ?")
print(f"{names[2].upper()}, how old are you now ?")
print(f"{names[-1].upper()}, thank you for respons !")
print()
#your own list 3-3
transportation = ["car", "motorcycle",]
print("i would like to own a "+ transportation[0].title())
print("i would like to own a "+transportation[1].title())
print()
#guest list from 3-4 to 3-7
inivitings = ["ayman", "ahmed", "mahmoud"]
print(f"Hi {inivitings[0].title()}, would you like to come to dinner with me ?")
print("hi "+inivitings[1]+", "+"would you like to come to dinner with me ?")
print(f"hi {inivitings[-1].title()}, would you like to come to dinner with me ?")
print()
inivitings[1]="medhat"
print(f"Hi {inivitings[0].title()}, would you like to come to dinner with me ?")
print("hi " +inivitings[1]+", "+"would you like to come to dinner with me ?")
print(f"hi {inivitings[-1].title()}, would you like to come to dinner with me ?")
print()
#guys i found more space tables
inivitings.insert(0,"khalad")
inivitings.insert(2,"gamal")
inivitings.append("yessein")
print(f"Hi {inivitings[0].title()}, would you like to come to dinner with me ?")
print("hi " +inivitings[1]+", "+"would you like to come to dinner with me ?")
print(f"hi {inivitings[2].title()}, would you like to come to dinner with me ?")
print(f"Hi {inivitings[3].title()}, would you like to come to dinner with me ?")
print("hi " +inivitings[4]+", "+"would you like to come to dinner with me ?")
print(f"hi {inivitings[5].title()}, would you like to come to dinner with me ?")
#i can only invite 2 people 
person_1 =inivitings.pop()
print(f"sorry, {person_1.title()}")
person_2 = inivitings.pop()
print(f"sorry, {person_2.title()}")
person_3 =inivitings.pop()
print(f"sorry, {person_3.title()}")
person_4 =inivitings.pop()
print(f"sorry, {person_4.title()}")
print(f"{inivitings[0].title()} you are still invited!")
print(f"{inivitings[-1].title()} you are still invited!")
del inivitings[0] , inivitings[0]
print(inivitings)
print()
#done 
#seeing the world 3-8
places = ["barchalona", "madried", "manchester", "london","paris"]
print(places)
print(sorted(places))
print(places) #it still in original oreder
places.reverse()
print(places)
places.reverse()
print(places) #back to original order
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print()
print(len(places)) #to know the lenth of a list 
