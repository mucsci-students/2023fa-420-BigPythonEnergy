import sys

if str(len(sys.argv) > 1 and sys.argv[1]) == "--cli":
    exec(open("BigPythonEnergy/MainCLI.py").read())

if str(len(sys.argv) > 1 and sys.argv[1]) == "--gui":
    exec(open("BigPythonEnergy/MainUI.py").read())

    
exec(open("BigPythonEnergy/MainUI.py").read())
