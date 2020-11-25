#name of class is always written in capital letter

#attributes are charecteristics of object
#methods are operation we can perform on object

class Dog():

    def __init__(self,breed):#initialisation
        self.breed=breed


mydog=Dog(breed="lab")
other_dog=Dog(breed="Huskie")
print(mydog.breed)
print(other_dog.breed)





class Dogie():

#class object attribute
    species="mammal"

    def __init__(self,breed,name):
        self.breed=breed
        self.name = name

mydogie=Dogie(breed="lab",name="bhau")
print("breed is :",mydogie.breed," name is:",mydogie.name,"And Specie is :",mydogie.species)
