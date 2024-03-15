import random

name = input("What is your first name?\n")
print("Hi", name , "I'm your fashion rater, Let's start from the top shall we?")

age = int(input("How old are you?\n"))
if age <= 10:
    print("I like your determination for new style")
elif age <= 17:
    print(age, "Is a good age to be exploring style")
else:
    print("It is never to late to explore")
#---------------------
print("")


hat = input("What hat's do you like\n")
randomHat = random.randint(1,3)
if randomHat == 1:
    print("I also think", hat , "are great.")
elif randomHat == 2:
    print("I don't know I think beanies are better")
else:
    print("Your taste could be better")
# ----------------------
print("")


sweater = input("What type of sweaters do you like?\n")
randomSweater = random.randint(1,3)
if randomSweater == 1:
    print("Me personally I think I like hoodies")
elif randomSweater == 2:
    print("I don't know I think hoodies are better")
else:
    print("Your taste could be better")
# ----------------------
print("")

pants = input("What kinds of pants do you like?\n")
print("I think", pants, "are absolutely fire!" )
response = input("")
randomResponse = random.randint(1,2)
if randomResponse == 1:
    print("I like where this is going")
else:
    print("I'm enjoying our conversations")
# ----------------------
print("")


last = input("I think that's all the time for today\n")
print("Well", name , "I had lots of fun today.")






