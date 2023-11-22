"""
This script determines if the current system supports a graphical user interface (GUI).
It checks the operating system (Windows, Linux, or macOS) and the availability of GUI libraries.
If GUI is supported, it can execute different Python scripts based on command line arguments.
Use "--cli" to run the command-line interface (CLI) and "--gui" to run the graphical user interface (GUI).
If neither argument is provided, it defaults to running the GUI.
"""
import sys
import platform

def is_gui_supported():
    system = platform.system()
    
    if system == "Windows":
        return True  # Windows generally supports GUI
    elif system == "Linux":
        # Check if X Window System (X11) is available
        try:
            import tkinter
            tkinter.Tk()
            return True
        except ImportError:
            return False
    elif system == "Darwin":  # macOS
        # Check for GUI environment (Aqua)
        return "Aqua" in platform.mac_ver()[0]
    
    return False  # Unknown system or unsupported

if is_gui_supported():
    if str(len(sys.argv) > 1 and sys.argv[1]) == "--cli":
        exec(open("BigPythonEnergy/MainCLI.py").read())

    elif str(len(sys.argv) > 1 and sys.argv[1]) == "--gui":
        exec(open("BigPythonEnergy/ViewGUI.py").read())

    else:
        exec(open("BigPythonEnergy/ViewGUI.py").read())
else:
    exec(open("BigPythonEnergy/MainCLI.py").read())
