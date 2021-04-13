#hidding of information and only giving access to a user to what is necessary.
class PlayerCharacter:

    def __init__(self,name,age):
        self.name = name #instance variable
        self.age = age

    def run(self):
        print('go '+ str(self.name))


    def shout(self):
        print(f"my name is {self.name} and age is {self.age}")

player1 = PlayerCharacter('CIndy',40)
player1.name = '!!!' #method overriding
player1.speak = 'Booooo'
print(player1.shout())
