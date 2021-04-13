class User():
    def __init__(self,email):
        self.email = email


    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the  power of {self.power}')



wizard1 = Wizard('bhau',100,'abc@gmail.com')

wizard1.attack()

print(wizard1.email)

# ------------------------------------------------------------------------

#alternatively we can use super keyword

class User():
    def __init__(self,email):
        self.email = email


    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email) #super means class above current class
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the  power of {self.power}')



wizard1 = Wizard('bhau',100,'abc@gmail.com')

wizard1.attack()

print(wizard1.email)
