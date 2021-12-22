import random
import sys
import mysql.connector
from datetime import datetime
import requests

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


def insertInDB(winnerDB, p1input, p2input, mydb):
    mycursor = mydb.cursor()
    sql = "insert into data (winner, p1pick, p2pick, playdate) values (%s, %s, %s, %s)"
    val = (winnerDB, p1input, p2input, datetime.now())
    mycursor.execute(sql, val)
    mydb.commit()


def getGameCount(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("select count(playdate) from data")
    myresult = mycursor.fetchone()
    for x in myresult:
        gameCount = x
    return gameCount


def optionData(option, mydb):
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


def winnerDataFromDB(mydb):
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


def createTable(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("create table if not exists data(winner varchar(2), p1pick varchar(10), p2pick varchar(10), playdate dateTime PRIMARY KEY)")
    return


def createDatabase():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root")
    mycursor = mydb.cursor()
    mycursor.execute("create database if not exists RPS")
    mydb.database = "RPS"
    return mydb


def sendRequest(username, voteScissors, voteRock, votePaper, voteSpock, voteLizard, apiIP = "http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl+= "?username=" + str(username) + "&voteScissors=" + str(voteScissors)
    reqUrl+= "&voteRock=" + str(voteRock) + "&votePaper=" + str(votePaper)
    reqUrl+= "&voteSpock=" + str(voteSpock) + "&voteLizard=" + str(voteLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode


def playerWinPrint(a):
    player1wins = 0
    player2wins = 0
    ties = 0
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


def optionsPrints():
    a = []
    for x in options:
        print(x + " picked * " + str(optionData(x, mydb)) + "; Pick-Percentage: " + str(round((optionData(x, mydb)/(getGameCount(mydb)*2)*100),2)) + "%")
        a.append(optionData(x, mydb))
    #api-request
    code = sendRequest("ng", a[2], a[0], a[1], a[3], a[4])
    print("Player 1 wins: " + str(winnerDataFromDB(mydb)[0]) + "; Win-Percentage: " + str(round((winnerDataFromDB(mydb)[0]/(getGameCount(mydb))*100),2)) + "%")
    print("Player 2 wins: " + str(winnerDataFromDB(mydb)[1]) + "; Win-Percentage: " + str(round((winnerDataFromDB(mydb)[1]/(getGameCount(mydb))*100),2)) + "%")
    print("Ties: " + str(winnerDataFromDB(mydb)[2]) + "; Percentage: " + str(round((winnerDataFromDB(mydb)[2]/(getGameCount(mydb))*100),2)) + "%")


if __name__ == '__main__':
    mydb = createDatabase()
    playercount = playerCount()
    yesNo = "y"
    createTable(mydb)
    while yesNo == "y":
        if playercount == 2:
            p1input, p2input = twoplayers()
        elif playercount == 1:
            p1input, p2input = oneplayer()
        p1Number = getNumber(p1input)
        p2Number = getNumber(p2input)
        playerWinPrint(defineWinner(p1Number, p2Number)[0])
        insertInDB(defineWinner(p1Number, p2Number)[1], p1input, p2input, mydb)
        yesNo = playAgain()
    print("Total number of games played: " + str(getGameCount(mydb)))
    optionsPrints()
    sys.exit(0)



