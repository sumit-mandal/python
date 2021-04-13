class PlayerCharacter:

    def __init__(self,name,age):
        self.name = name #instance variable
        self.age = age

    def run(self):
        print('go '+ str(self.name))


    def shout(self):
        print(f"my name is {self.name} and age is {self.age}")

cindy = input("Enter your name")
age1 = int(input("Enter your age"))

player1 = PlayerCharacter(cindy,age1)
player1.name = '!!!' #method overriding
player1.speak = 'Booooo'
print(player1.shout())
