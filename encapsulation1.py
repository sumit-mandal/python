#encapsulation means packing inside the box
class PlayerCharacter:

    def __init__(self,name,age):
        self.name = name #instance variable
        self.age = age

    def run(self):
        print('go '+ str(self.name))


    def shout(self):
        print(f"my name is {self.name} and age is {self.age}")

player1 = PlayerCharacter('CIndy',40)
# player2 = PlayerCharacter('Tom',21)



player1.shout()
player1.run()
