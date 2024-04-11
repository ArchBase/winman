import tkinter as tk
import threading
import time



class Blocker:
    def __init__(self) -> None:
        self.root = None
    def block_screen(self):
        self.root = tk.Tk()
        self.root.title("Fullscreen Window")

        # Set background color to dark
        self.root.configure(bg="#000000")
        self.root.config(cursor="none")
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set the window size to fullscreen
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Make the window non-exitable
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)

        label = tk.Label(self.root, text="Sorry, Your not my master!", font=("Helvetica", 24), fg="red", bg="#000000")
        label.pack(expand=True)

        # Run the application
        self.root.mainloop()
    def release_screen(self):
        # Wait for 5 seconds
        #time.sleep(5)
        # Close the fullscreen window
        self.root.quit()

