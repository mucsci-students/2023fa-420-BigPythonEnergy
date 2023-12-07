# 2023fa-420-BigPythonEnergy
Spelling Bee Created by Big Python Energy.
v0.1
Brendan LeFevre
Rose Mattaboni
Sean McQuillen
Vasilis B

Use our build system to run the game!

Instructions for setting up the build system:

    1.  After pulling the repository from GitHub, navigate to the main project 
        directory in a command line terminal. The main directory contains 
        'BigPythonEnergy', 'requirements.txt', etc... 
        Now the first step is to set up a virtual environment (if you do not 
        already have one set up). To do this, simply run:
        > python -m venv venv


    2.  The next step is to activate the virtual environment (venv). 
        To do this run an activate command. There are several ways to do this:

        a. If you are using VS code and would like to operate from the 
           integrated powershell terminal run the following commands to 
           activate the venv:
            > Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
            > ./venv/Scripts/Activate.ps1

        b. If you are using a windows type machine and do not want to use 
           powershell, or are otherwise unable to run powershell, 
           execute the following command to activate the venv:
            > venv\Scripts\Activate.bat

        c. If you are using a linux/mac type machine, run the following 
           command to activate the venv:
            > source venv/bin/activate


    3.  The next step is to download the project dependancies into your 
        virtual environment (venv). To do this,
        simply run the following command:
        > pip3 install -r requirements.txt


    4.  Now your virtual environment is open and setup with the proper 
        dependancies and you are ready to play the game. 
        To play in the command line:
            > python BigPythonEnergy/execute66.py --cli

        To play using the GUI:
            > python BigPythonEnergy/execute66.py --gui

        If neither is specified, the game will start in the GUI if your system 
        supports it. If not, it will start in the command line.
    

    5.  When you have completed the game to your satisfaction and want to close
        the virtual environment, simply run a "deactivate" command to return to
        your native environment:
        > deactivate

Have fun!

Design Patterns:

1.  Facade (Structural): A single class that represents an entire subsystem. 
    In our project we are utilizing a dictionary interface class which is 
    responsible for all word comparison, generation, and manipulation in the 
    puzzle. The DictInterface Class is responsible for:
        Checking if a guess is valid; meaning it contains the required letter
        and only the acceptable letters.
        Generating a list of valid words; all words made up of the required
        and acceptable letters
        Has the functionality to select a random word made up of only 7 unique
        letters; if a user wants to play with a randomly generated puzzle
    All intensive hint logic:
        Find counts for all pangrams and perfect pangrams
        Count the number of valid words starting with a given 2 letter combo
        Generate bingo sheet and find all values:
            Number of words starting with every letter from lengths 4-15
            Calculate all sigma values in the bingo sheet
    This class allows us to interact with the dictionary without concern 
    for the specifics of the implementation. 
    
2.  Model-View-Controller (Structural): A set of classes that split most of the
    background classes into model, view, or controller as specified in general
    programming logic. Model is responsible for:
        The Puzzle class, which handles all of the logic and storage for an
        instance of a puzzle, 
        the DictInterface class, which is a facade that handles all 
        interactions with the dictionary,
        and the Scoreboard class, which handles interactions that involve the 
        scoreboard.
    View is responsible for:
        the ViewCLI class, which contains all of the repetitive or large text 
        for usage in the CLI. This also contains the tab completion.
    Outside of these two files, MainCLI and MainGameCLI handle controller 
    for the command line and run as themselves. In contrast, controller for 
    GUI is handled as an object (MainUI) while view is the main file that runs
    (ViewGUI) as well as the UI files it calls (which are both MainWindowUI 
    and the files in the ui folder).

3.  Builder (Creational): A full file with multiple classes that allows for 
    creation for modular objects. In this case, it is used for the creation 
    of only two types of objects, a full puzzle and a null puzzle 
    (represented by null object behavior). It chooses which to create based
    on inputs and allows the Puzzle class to interface with whichever one
    was built through means of an abstract puzzle. This is used for creation of
    null puzzles under the right circumstances.

4.  Null Object (Behavioral): A single class within the PuzzleBuilder file 
    that allows for a null version of the Puzzle class. This has its uses 
    when the GUI needs to load text or handle actions that can only be done 
    when a puzzle is not null while still keeping an active puzzle ready 
    from the start.

5.  Singleton (Creational): A class that exists only as a single instance 
    that is globally accessible. In our project, this is used with our Model
    class to ensure that there are no duplicate puzzles or duplicate 
    instantiations of the facade (DictInterface). This keeps there from being
    multiple puzzles or multiple points of entry to interfacing the dictionary,
    things that could be very confusing to keep track of and would not be 
    necessary for this game.

6.  State (Behavioral): A variable that exists in the ViewGUI file that, when 
    changed, causes our GUI view to switch to a secret congratulatory game 
    state for those who find all words in a puzzle. This is used within our 
    program for when the game is completely finished to inform users that 
    they have won and to keep them from making guesses.


Code Map (UML):


Entry point -> execute66.py

GUI ->

    View -> ViewGUI.py (main) -> MainWindowUI.py

    Controller -> MainUI.py

CLI ->

    View -> View.py -> ViewCLI.py

    Controller -> MainCLI.py (main) -> MainGameCLI.py

Model ->

    Model.py ->

        DictInterface.py, Puzzle.py -> PuzzleBuilder.py, scoreboard.py

Tests ->

    Tests.py
