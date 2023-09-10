import os

# Main screen loop for getting the user around the application, can go to the start screen, the help screen, or quit the application
def inputCheck():
    print('Please enter "Start" to begin a game, "Help" for a help page, or "Quit" to leave the game.') 
    userInput = input()
    userInput = userInput.lower() #turns the user input into lower case for type checking
    
    if userInput == "start":
        startPage()
    elif userInput == "help":
        helpPage()
    elif userInput == "quit":
        exit()
    else:
        print('unrecognized command, please try again:')
        inputCheck()

#Start page where the user can select what type of puzzle they want, or they can go back to the main screen
def startPage():
    print('Welcome to the start page, enter "Random" to start from a random word, "Load" to start from a save file, or "Choose" to started from your own Chosen word.')
    print('Or enter "Back" to go back to the start page')
    userInput = input()
    userInput = userInput.lower() #turns the user input into lower case for type checking

    if userInput == "random":
        print('random')

    if userInput == "load":
        print('load')

    if userInput == "choose":
        print('choose')

    if userInput == "back":
        inputCheck()
    
    else:
        print('unknown command, please enter another')
        startPage()



#help page is used if the user wants some more information
def helpPage():
    print('---------------------------------------------------------------------------------------------------------------------')
    print('Help Page:')
    print('This is a spelling bee game, the objective of the game is to spell out at many words as possible.')
    print('The guessed word must have atleast 4 letter, it must be a valid word, you can only use the letters given to create your words, and the middle letter must be used.')
    print('You can reuse letters as many times as you need to create your word.')
    print('As you find more words, you will get points, and as you get enough points, you will increase in rank.')
    print('Points:')
    print('4 Letter word = 1 point. 5 Letter word = 5 points. 6 Letter word = 6 points, and so on.')
    print('Use all 7 letters given = 7 extra points.')
    print('Rank thresholds are based on the total number of words possible.')
    print('---------------------------------------------------------------------------------------------------------------------')
    print('Please enter "Start" to begin a game, "Help" for a help page, or "Quit" to leave the game.') 
    inputCheck()

#Start script to clear the command line so the user just sees the instructions.
os.system('cls')
print('--------------------------------')
print('Welcome to Spelling Bee!')
print('Created by Big Python Energy!')
print('--------------------------------')
inputCheck()


