import random
print("Play Rock, Paper, scissors against AI. If you wish to exit type: end")
user = input()
choices = ['rock', 'paper', 'scissors']
t = random.choice(choices)
 
def decider(user, t): 
    if user == 'rock' and t == "paper":
        return "Oops You Lost."
    else:
        return "Bravo You Won!" 
    if user == 'paper' and t == "scissors":
        return "Oops You Lost."
    else:
        return "Bravo You Won!" 
    if user == 'scissors' and t == "rock":
        return "Oops You Lost."
    else:
        return "Bravo You Won!"
    
while user != "end":
    user = input("Make a choice")
    t = random.choice(choices) 
    if user == "end":
        print("Game Over.") 
    elif user not in choices:
        print("Input Error: Input not valid choice. Choose again.")
    elif user == t:
        print("Draw")
    else:
        print(decider(user, t))                
