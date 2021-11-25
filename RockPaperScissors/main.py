import random
import sys
import mysql.connector
from datetime import datetime

options = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alfa1919",
    database="RPS")


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
    winnerDB = ""
    if (input1 - input2) == 0:
        return "Tie", "x"
    elif (input1 - input2) % len(options) % 2 == 1:
        winnerDB = "p1"
        return "Player 1 Wins", winnerDB
    elif ((input1 - input2) % len(options)) % 2 == 0:
        winnerDB = "p2"
        return "Player 2 Wins", winnerDB



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
        if yesNo == "y":
            return yesNo
        if yesNo == "n":
            return yesNo

def insertInDB(winnerDB, p1input, p2input):
    mycursor = mydb.cursor()
    sql = "insert into data (winner, p1pick, p2pick, playdate) values (%s, %s, %s, %s)"
    val = (winnerDB, p1input, p2input, datetime.now())
    mycursor.execute(sql, val)
    mydb.commit()


def getGameCount():
    mycursor = mydb.cursor()
    mycursor.execute("select count(playdate) from data")
    myresult = mycursor.fetchone()
    for x in myresult:
        gameCount = x
    return gameCount


def optionData(option):
    mycursor = mydb.cursor(buffered=True)
    mycursor2 = mydb.cursor(buffered=True)
    mycursor.execute("select count(playdate) from data where p1pick = '" + option + "'")
    mycursor2.execute("select count(playdate) from data where p2pick = '" + option + "'")
    myresult = mycursor.fetchone()
    myresult2 = mycursor2.fetchone()
    for x in myresult:
        optionCount = x
    for y in myresult2:
        optionCount += y
    return optionCount


def winnerDataFromDB():
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("select count(playdate) from data where winner = 'p1'")
    myresult = mycursor.fetchone()
    for x in myresult:
        p1Wins = x
    mycursor.execute("select count(playdate) from data where winner = 'p2'")
    myresult = mycursor.fetchone()
    for x in myresult:
        p2Wins = x
    mycursor.execute("select count(playdate) from data where winner = 'x'")
    myresult = mycursor.fetchone()
    for x in myresult:
        Ties = x
    return p1Wins, p2Wins, Ties


if __name__ == '__main__':
    player1wins = 0
    player2wins = 0
    ties = 0
    playercount = playerCount()
    yesNo = "y"
    p1input = ""
    p2input = ""
    while yesNo == "y":
        if playercount == 2:
            p1input, p2input = twoplayers()
        elif playercount == 1:
            p1input, p2input = oneplayer()
        p1Number = getNumber(p1input)
        p2Number = getNumber(p2input)
        a = defineWinner(p1Number, p2Number)[0]
        print(a)
        if a == "Player 1 Wins":
            player1wins += 1
        if a == "Player 2 Wins":
            player2wins += 1
        if a == "Tie":
            ties += 1
        print("Player 1 wins: " + str(player1wins))
        print("Player 2 wins: " + str(player2wins))
        print("Ties: " + str(ties))
        insertInDB(defineWinner(p1Number, p2Number)[1], p1input, p2input)
        yesNo = playAgain()
    print("Total number of games played: " + str(getGameCount()))
    for x in options:
        print(x + " picked * " + str(optionData(x)) + "; Pick-Percentage: " + str(round((optionData(x)/(getGameCount()*2)*100),2)) + "%")
    print("Player 1 wins: " + str(winnerDataFromDB()[0]) + "; Win-Percentage: " + str(round((winnerDataFromDB()[0]/(getGameCount()*2)*100),2)) + "%")
    print("Player 2 wins: " + str(winnerDataFromDB()[1]) + "; Win-Percentage: " + str(round((winnerDataFromDB()[1]/(getGameCount()*2)*100),2)) + "%")
    print("Ties: " + str(winnerDataFromDB()[2]) + "; Percentage: " + str(round((winnerDataFromDB()[2]/(getGameCount()*2)*100),2)) + "%")
    sys.exit(0)



