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

    if str(len(sys.argv) > 1 and sys.argv[1]) == "--gui":
        exec(open("BigPythonEnergy/MainUI.py").read())


    exec(open("BigPythonEnergy/MainUI.py").read())

exec(open("BigPythonEnergy/MainCLI.py").read())


