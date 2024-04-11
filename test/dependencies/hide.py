import subprocess
import sys
import ctypes

def hide_cmd():
    if sys.platform.startswith('win'):
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        SW_HIDE = 0
        hWnd = kernel32.GetConsoleWindow()
        if hWnd:
            user32.ShowWindow(hWnd, SW_HIDE)
        subprocess.Popen([sys.executable, __file__], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        print("This feature is only supported on Windows.")

if __name__ == "__main__":
    hide_cmd()
