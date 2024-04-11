import tkinter as tk
import threading
import time

root = None

def fullscreen_window():
    global root
    # Create the fullscreen window
    root = tk.Tk()
    root.title("Fullscreen Window")

    # Set background color to dark
    root.configure(bg="#000000")
    root.config(cursor="none")
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to fullscreen
    #root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Make the window non-exitable
    root.attributes("-topmost", True)
    root.attributes("-fullscreen", True)

    label = tk.Label(root, text="Sorry, Your not my master!", font=("Helvetica", 24), fg="red", bg="#000000")
    label.pack(expand=True)

    # Run the application
    root.mainloop()

def close_fullscreen_window():
    global root
    # Wait for 5 seconds
    time.sleep(5)
    # Close the fullscreen window
    root.quit()

# Create a separate thread for the fullscreen window
fullscreen_thread = threading.Thread(target=fullscreen_window)
fullscreen_thread.start()
#time.sleep(5)
# Wait for 5 seconds in the main thread and then close the window
close_fullscreen_thread = threading.Thread(target=close_fullscreen_window)
close_fullscreen_thread.start()

# Join the threads to wait for them to finish
fullscreen_thread.join()
close_fullscreen_thread.join()
