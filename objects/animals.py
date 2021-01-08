# animals.py
# a look at object-oriented programming

class Animal():
    # CONSTRUCTOR
    def __init__(self):
        self.legs = 0
        self.hairy = False

    def talk(self):
        return "Hello."

    def eat(self, food):
        if food == "meat":
            return("Yummm. Meat.")
        elif food in["Veggies", "Vegetables"]:
            return("Yummm. Vegetables.")
        else:
            return("Poo")
dog = Animal()
dog.legs = 4
dog.hairy = True
print(dog.legs)

# if dog.hairy:
#   print("You'll need to brush its hair")

print(dog.talk())
print(dog.eat("meat"))