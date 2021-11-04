import random
import sys

options = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def checkInput(userInput):
    if userInput in options:
        return False
    return True


def playerCount():
    falseCount = True
    while (falseCount):
        print("1 or 2 Players?")
        playerCountInput = input()
        if playerCountInput == "1":
            playercount = 1
            falseCount = False
        elif playerCountInput == "2":
            playercount = 2
            falseCount = False
        else:
            print("Wrong input")
    return playercount


def getNumber(userinput):
    number = options.index(userinput)
    return number


def defineWinner(input1, input2):
    if (input1 - input2) == 0:
        return "Tie"
    elif (input1 - input2) % len(options) % 2 == 1:
        return "Player 1 Wins"
    elif ((input1 - input2) % len(options)) % 2 == 0:
        return "Player 2 Wins"


def oneplayer():
    p1input = ""
    while checkInput(p1input):
        print("Player 1 Input:")
        p1input = input()
    p2input = random.choice(options)
    print("Computer-Input: " + p2input)
    return p1input, p2input


def twoplayers():
    p1input = ""
    p2input = ""
    while checkInput(p1input):
        print("Player 1 Input:")
        p1input = input()
    for i in range(20):
        print("\n")
    while checkInput(p2input):
        print("Player 2 Input:")
        p2input = input()
    return p1input, p2input


def playAgain():
    while True:
        print("Play again? y/n")
        yesNo = input()
        if (yesNo == "y"):
            return yesNo
        if (yesNo == "n"):
            return yesNo


if __name__ == '__main__':
    playercount = playerCount()
    yesNo = "y"
    p1input = ""
    p2input = ""
    while (yesNo == "y"):
        if playercount == 2:
            p1input, p2input = twoplayers()
        elif playercount == 1:
            p1input, p2input = oneplayer()
        p1Number = getNumber(p1input)
        p2Number = getNumber(p2input)
        print(defineWinner(p1Number, p2Number))
        yesNo = playAgain()
    sys.exit(0)
