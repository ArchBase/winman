import tkinter as tk
import threading



class Face_Login:
    def __init__(self) -> None:
        self.root = None
    def block_screen(self):
        def fullscreen_window(self):
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
            #self.root.geometry("100x100")

            # Make the window non-exitable
            self.root.attributes("-topmost", True)
            self.root.attributes("-fullscreen", True)

            label = tk.Label(self.root, text="Recognizing face...", font=("Helvetica", 24), fg="red", bg="#000000")
            label.pack(expand=True)

            # Run the application
            self.root.mainloop()
        self.fullscreen_thread = threading.Thread(target=fullscreen_window, args=(self, ))
        self.fullscreen_thread.start()

    def release_screen(self):
        # Wait for 5 seconds
        #time.sleep(5)
        # Close the fullscreen window
        self.root.quit()



import cv2
import globals_config as gb
import time
import login



class Session_Manager:
    def __init__(self) -> None:
        self.is_section_open = True
        self.blocker = Face_Login()
        self.authenticator = login.Authenticator()
    def mainloop(self):
        self.blocker.block_screen()
        cap = cv2.VideoCapture(0)
        try:
            while True:
                #time.sleep(gb.config["delay"])
                # Read a frame from the webcam
                ret, frame = cap.read()
                
                # Convert the frame to grayscale
                #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                self.authenticator.verify_using_camera(frame)

                if self.authenticator.verified:
                    self.blocker.release_screen()
                    cap.release()
                    break

        except KeyboardInterrupt:
            cap.release()

mgr = Session_Manager()
mgr.mainloop()