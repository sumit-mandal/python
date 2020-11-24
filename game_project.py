import random
#get guess
def get_guess():
    return list(input("What is your guess :\n"))




#genrate computer code 123

def generate_code():
    digits=[str(num) for num in range (10)]

    #Shuffle the digits
    #then grab the first three
    random.shuffle(digits)
    return digits[:3]


#generate the clues

def generate_clues(code,user_guess):

    if user_guess==code:
        return "CODE CRACKED!"

    clues = []



    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")


    if clues==[]:
        return["Nope"]
    else:
        return clues





#run game logic

print("Welcome Code Breaker!")

secret_code=generate_code()

clue_report=[]

while clue_report !="Code CRACKED!":

    guess=get_guess()

    clue_report=generate_clues(guess,secret_code)
    print("Here is the result of your guess:")

    for clue in clue_report:
        print(clue)
