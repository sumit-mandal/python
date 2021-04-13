class PlayerCharacter:
    #Class object attribute
    membership = True
    def __init__(self,name,age):
        if self.membership:
            self.name = name #instance variable
            self.age = age
    def shout(self):
        print(f"my name is {self.name}")

player1 = PlayerCharacter('CIndy',40)
player2 = PlayerCharacter('Tom',21)
player2.attack = 50

print(player1.shout())

#class object atrribute doesn't change arounnd it's instances and always remains static.
# A variable that is defined inside a method and belongs only to the current instance of a class.
# Class variable − A variable that is shared by all instances of a class. Class variables are defined
 # within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
