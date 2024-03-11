# Game Project Template

# Imports for additiona functionality
import sys
import random
import time

# ====================================================================

# Game functions

def startGame():
    initGlobals()
    getPlayerName()
    Instructions()
    gameLoop()

# declare globals first
def initGlobals():
    global playerName
    global playerY
    global playerX
    global turns
    global ObstacleOneX
    global ObstacleOneY
    global ObstacleTwoX
    global ObstacleTwoY
    global ObstacleThreeX
    global ObstacleThreeY
    global treasureX
    global treasureY
    playerName = ""
    playerX = 2
    playerY = 2
    treasureX = random.randint(0, 5)  # Make sure this is randomized before submitting
    treasureY = random.randint(0, 5)  # Make sure this is randomized before submitting
    ObstacleOneX = random.randint(0, 4)
    ObstacleOneY = random.randint(0, 4)
    ObstacleTwoX = random.randint(0, 4)
    ObstacleTwoY = random.randint(0, 4)
    ObstacleThreeX = random.randint(0, 4)
    ObstacleThreeY = random.randint(0, 4)
    turns = 20

# get player's name

def getPlayerName():
    namelength = False
    global playerName
    time.sleep(1)
    print("Welcome to LEGEND OF PYTHON")
    while namelength == False:
        time.sleep(1.5)
        playerName = input("What is your name? ")
        if len(playerName) >= 3:
            namelength = True
            playerName = playerName.capitalize()
        else:
            namelength = False
            time.sleep(1.5)
            print("Name isn't long enough, please try again.")
    return playerName

#provide instructions

def Instructions():
    global playerName
    time.sleep(1.5)
    print("Your mission,", playerName, "is to defeat Ganondorf and save Hyrule before it's too late.")
    time.sleep(2.4)
    print("You will have 20 turns to do so and will come across various obstacles to keep going.")
    time.sleep(2.4)
    print("You will be using U, D, L, and R to move across the map. Good luck!")


# See if they found the treasure
def isTreasure():
    global playerX
    global playerY
    global treasureX
    global treasureY
    if (playerX, playerY) == (treasureX, treasureY):
        print("You have arrived at the castle...")
        time.sleep(1.5)
        print("Ganondorf has emerged and transforms into Ganon!")
        time.sleep(1.5)
        print("To defeat this beast, answer this riddle:")
        finalQuestion()

# final obstacle
def finalQuestion():
    counter = 0
    retVal = False
    while counter < 3:
        time.sleep(1.5)
        ans = input("Where does Zelda find her heroes? ")
        if ans == "Linkedin" or ans == "linkedin":
            counter += 3
            time.sleep(1.5)
            print("You unleash the power from your Master Sword upon Ganon and he transforms back into Ganondorf.")
            time.sleep(2)
            print("Zelda seals him into the Sacred Realm and Hyrule will no longer be under Ganondorf's rule.")
            time.sleep(3)
            print("For now...")
            time.sleep(2)
            ans = input("Do you want to play again? ")
            ans = ans.capitalize()
            if ans == "Yes" or ans == "Y":
                time.sleep(1.5)
                print("Great! Let's play!")
                startGame()
            else:
                time.sleep(1.5)
                print("Thanks for playing!")                
                sys.exit()
            retVal = True
        elif ans == "LINKEDIN" or ans == "LinkedIn":
            counter += 3
            time.sleep(1.5)
            print("You unleash the power from your Master Sword upon Ganon and he transforms back into Ganondorf.")
            time.sleep(2)
            print("Zelda seals him into the Sacred Realm and Hyrule will no longer be under Ganondorf's rule.")
            time.sleep(3)
            print("For now...")
            time.sleep(2)
            ans = input("Do you want to play again? ")
            ans = ans.capitalize()
            if ans == "Yes" or ans == "Y":
                time.sleep(1.5)
                print("Great! Let's play!")
                startGame()
            else:
                time.sleep(1.5)
                print("Thanks for playing!")                
                sys.exit()
            retVal = True
        else:
            counter += 1
            retVal = False
            if counter == 2:
                time.sleep(1.5)
                print("You only have one guess left, here's a hint.")
                time.sleep(1.5)
                print("It's a famous website for employers.")
            if counter == 3:
                time.sleep(1.5)
                print("You've guessed too many times.")
                time.sleep(1.5)
                print("You were unable to defeat Ganondorf and save Hyrule :[")
                time.sleep(1.5)
                print("------------ GAME OVER ------------")
                time.sleep(1.5)
                ans = input("Do you want to play again? ")
                ans = ans.capitalize()
                if ans == "Yes" or ans == "Y":
                    time.sleep(1.5)
                    print("Great! Let's play!")
                    startGame()
                else:
                    time.sleep(1.5)
                    print("Thanks for playing!")                    
                    sys.exit()
            else:
                time.sleep(1.5)
                print("Guess again.")

# create function for obstacles

#1st obstacle
def numberGuess():
    time.sleep(2)
    print("To pull out the Master Sword, guess a number between 1 and 5. You only have three chances.")
    counter = 0
    number = random.randint(1, 5)
    retVal = False
    while counter < 3:
        time.sleep(2)
        ans = int(input("What's your guess? "))
        if ans == number:
            counter += 3
            retVal = True
            time.sleep(1.5)
            print("You have pulled the Master Sword out but Ganondorf snuck behind you and claimed the Triforce!")
            time.sleep(1.5)
            print("Find and defeat him before it's too late!")
        else:
            counter += 1
            retVal = False
            if counter == 3:
                time.sleep(1.5)
                print("You've guessed too many times.")
                time.sleep(1.5)
                print("------------ GAME OVER ------------")
                time.sleep(1.5)
                ans = input("Do you want to play again? ")
                ans = ans.capitalize()
                if ans == "Yes" or ans == "Y":
                    time.sleep(1.5)
                    print("Great! Let's play!")
                    startGame()
                else:
                    time.sleep(1.5)
                    print("Thanks for playing!")                    
                    sys.exit()
            else:
                time.sleep(2)
                print("Sorry that answer is wrong. Try again")
    return retVal

# second obstacle
def mathQuiz():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    sum = a + b
    counter = 0
    retVal = False
    time.sleep(1.5)
    print("To use your Ocarina and play her song, tell me the sum of", a ,"and", b)
    while counter < 3:
        time.sleep(1.5)
        ans = int(input("What's your answer? "))
        if ans != sum:
            counter += 1
            retVal = False
            if counter == 3:
                time.sleep(1.5)
                print("You've guessed too many times.")
                time.sleep(1.5)
                print("------------ GAME OVER ------------")
                time.sleep(1.5)
                ans = input("Do you want to play again? ")
                ans = ans.capitalize()
                if ans == "Yes" or ans == "Y":
                    time.sleep(1.5)
                    print("Great! Let's play!")
                    startGame()
                else:
                    time.sleep(1.5)
                    print("Thanks for playing!")                    
                    sys.exit()
            else:
                time.sleep(1.5)
                print("Wrong, try again.")
        else:
            counter += 3
            retVal = True
            time.sleep(1.5)
            print("Epona came to you, ready to help you defeat Ganondorf!")
    return retVal

#third obstacle
def TrueorFalse():
    counter = 0
    retVal = False
    time.sleep(1.5)
    print("To gain her trust, answer this True or False question by typing T for True and F for False.")
    while counter < 3:
        time.sleep(2)
        ans = input("6 out of 10 parents prefer their children to learn Python instead of French, True or False? ")
        if ans == "T":
            counter += 3
            retVal = True
            time.sleep(1.5)
            print("Sheik has revealed herself as Zelda and is ready to help you defeat Ganondorf!")
        elif ans == "F":
            counter += 1
            retVal = False
            if counter == 3:
                time.sleep(1.5)
                print("You've guessed too many times.")
                time.sleep(1.5)
                print("------------ GAME OVER ------------")
                time.sleep(1.5)
                ans = input("Do you want to play again? ")
                ans = ans.capitalize()
                if ans == "Yes" or ans == "Y":
                    time.sleep(1.5)
                    print("Great! Let's play!")
                    startGame()
                else:
                    time.sleep(1.5)
                    print("Thanks for playing!")
                    sys.exit()
            else:
                time.sleep(1.5)
                print("Sorry that answer is wrong. Try again.")
        else:
            time.sleep(1.5)
            print("Incorrect input, please type T or F.")
    return retVal
# create function to check their location for an obstacle

def CheckForObstacle():
    global playerX
    global playerY
    global ObstacleOneX
    global ObstacleOneY
    global ObstacleTwoX
    global ObstacleTwoY
    global ObstacleThreeX
    global ObstacleThreeY
    if (playerX, playerY) == (ObstacleOneX, ObstacleOneY):
        time.sleep(1.5)
        print("You've reached the Temple of Time.")
        numberGuess()
    elif (playerX, playerY) == (ObstacleTwoX, ObstacleTwoY):
        time.sleep(1.5)
        print("You arrive at Lon Lon Ranch and see your beloved horse, Epona.")
        mathQuiz()
    elif (playerX, playerY) == (ObstacleThreeX, ObstacleThreeY):
        time.sleep(1.5)
        print("A mysterious woman named Sheik appears but is hesitant to guide you.")
        TrueorFalse()

def movePlayer(direction):
    global playerY
    global playerX
    global playerName
    retVal = False
    if (direction == "U"):
        if playerY == 4:
            retVal = False
            time.sleep(1.5)
            print("You can't go that way or you'll fall off the map! Lose a turn.")
        else:
            retVal = True
            playerY += 1
            isTreasure()
            CheckForObstacle()
            time.sleep(1.5)
            print(playerName, "moved up one space.")
    if (direction == "D"):
        if playerY == 0:
            retVal = False
            time.sleep(1.5)
            print("You can't go that way or you'll fall off the map! Lose a turn.")
        else:
            retVal = True
            playerY -= 1
            isTreasure()
            CheckForObstacle()
            time.sleep(1.5)
            print(playerName, "moved down one space.")
    if (direction == "L"):
        if playerX == 0:
            retVal = False
            time.sleep(1.5)
            print("You can't go that way or you'll fall off the map! Lose a turn.")
        else:
            retVal = True
            playerX -= 1
            isTreasure()
            CheckForObstacle()
            time.sleep(1.5)
            print(playerName, "moved left one space.")
    if (direction == "R"):
        if playerX == 4:
            retVal = False
            time.sleep(1.5)
            print("You can't go that way or you'll fall off the map! Lose a turn.")
        else:
            retVal = True
            playerX += 1
            isTreasure()
            CheckForObstacle()
            time.sleep(1.5)
            print(playerName, "moved right one space.")

    return retVal

def gameLoop():
    global turns
    while turns >= 0:
        getPlayerMove()
    else:
        time.sleep(1.5)
        print("You've used all your turns.")
        time.sleep(1.5)
        print("------------ GAME OVER ------------")
        time.sleep(1.5)
        ans = input("Do you want to play again? ")
        ans = ans.capitalize()
        if ans == "Yes" or "Y":
            time.sleep(1.5)
            print("Great! Let's play!")
            startGame()
        else:
            time.sleep(1.5)
            print("Thanks for playing!")            
            sys.exit()

def getPlayerMove():
    global turns
    while turns != 0:
        time.sleep(1.5)
        ans = input("In which direction would you like to move? ")
        if ans == "U" or ans == "u":
            ans = ans.capitalize()
            turns -= 1
            if turns == 1:
                print("You only have 1 turn left!")
                if turns == 0:
                    time.sleep(1.5)
                    print("You've used all your turns.")
                    time.sleep(1.5)
                    print("------------ GAME OVER ------------")
                    time.sleep(1.5)
                    ans = input("Do you want to play again? ")
                    ans = ans.capitalize()
                    if ans == "Yes" or "Y":
                        time.sleep(1.5)
                        print("Great! Let's play!")
                        startGame()
                    else:
                        time.sleep(1.5)
                        print("Thanks for playing!")                        
                        sys.exit()
            else:
                movePlayer("U")
                time.sleep(1.5)
                print("There are", turns, "turns remaining.")
        elif ans == "D" or ans == "d":
            ans = ans.capitalize()
            turns -= 1
            if turns == 1:
                print("You only have 1 turn left!")
                if turns == 0:
                    time.sleep(1.5)
                    print("You've used all your turns.")
                    time.sleep(1.5)
                    print("------------ GAME OVER ------------")
                    time.sleep(1.5)
                    ans = input("Do you want to play again? ")
                    ans = ans.capitalize()
                    if ans == "Yes" or "Y":
                        time.sleep(1.5)
                        print("Great! Let's play!")
                        startGame()
                    else:
                        time.sleep(1.5)
                        print("Thanks for playing!")                        
                        sys.exit()
            else:
                movePlayer("D")
                time.sleep(1.5)
                print("There are", turns, "turns remaining.")
        elif ans == "R" or ans == "r":
            ans = ans.capitalize()
            turns -= 1
            if turns == 1:
                print("You only have 1 turn left!")
                if turns == 0:
                    time.sleep(1.5)
                    print("You've used all your turns.")
                    time.sleep(1.5)
                    print("------------ GAME OVER ------------")
                    time.sleep(1.5)
                    ans = input("Do you want to play again? ")
                    ans = ans.capitalize()
                    if ans == "Yes" or "Y":
                        time.sleep(1.5)
                        print("Great! Let's play!")
                        startGame()
                    else:
                        time.sleep(1.5)
                        print("Thanks for playing!")
                        sys.exit()
            else:
                movePlayer("R")
                time.sleep(1.5)
                print("There are", turns, "turns remaining.")
        elif ans == "L" or ans == "l":
            ans = ans.capitalize()
            turns = turns - 1
            if turns == 1:
                print("You only have 1 turn left!")
                if turns == 0:
                    time.sleep(1.5)
                    print("You've used all your turns.")
                    time.sleep(1.5)
                    print("------------ GAME OVER ------------")
                    time.sleep(1.5)
                    ans = input("Do you want to play again? ")
                    ans = ans.capitalize()
                    if ans == "Yes" or "Y":
                        time.sleep(1.5)
                        print("Great! Let's play!")
                        startGame()
                    else:
                        time.sleep(1.5)
                        print("Thanks for playing!")                        
                        sys.exit()
            else:
                movePlayer("L")
                time.sleep(1.5)
                print("There are", turns, "turns remaining.")
        else:
            time.sleep(1.5)
            print("Incorrect input. Try again.")

    return ans



def main():
    startGame()

main()
