import random

if __name__ == '__main__':
    options = ["Rock", "Paper", "Scissor", "Spock", "Lizard"]
    userinput = "Rock"
    userwin = 0

    selection = random.choice(options)
    print(selection)
    if(userinput == selection):
        print("Tie")
    if(userinput == "Rock"):
        if(selection == "Paper"):
            print("Lose for User")
            userwin = 1
        if(selection=="Spock"):
            print("Lose for User")
            userwin = 1

    if (userinput == "Paper"):
        if (selection == "Scissors"):
            userwin = 1
            print("Lose for User")
        if (selection == "Lizard"):
            userwin = 1
            print("Lose for User")

    if (userinput == "Scissors"):
        if (selection == "Rock"):
            userwin = 1
            print("Lose for User")
        if (selection == "Spock"):
            userwin = 1
            print("Lose for User")

    if (userinput == "Lizard"):
        if (selection == "Rock"):
            userwin = 1
            print("Lose for User")
        if (selection == "Scissors"):
            userwin = 1
            print("Lose for User")

    if (userinput == "Spock"):
        if (selection == "Lizard"):
            userwin = 1
            print("Lose for User")
        if (selection == "Paper"):
            userwin = 1
            print("Lose for User")

    if(userwin==0):
        print("User wins")


