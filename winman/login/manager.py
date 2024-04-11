import cv2
import window
import login
import globals_config as gb
import time



class Session_Manager:
    def __init__(self) -> None:
        self.is_section_open = False
        self.authenticator = login.Authenticator()
        self.blocker = window.Blocker()
    def mainloop(self):
        cap = cv2.VideoCapture(0)
        while True:
            time.sleep(gb.config["delay"])
            # Read a frame from the webcam
            ret, frame = cap.read()
            
            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.authenticator.verify_using_camera(gray_frame)

            if self.authenticator.is_verified_now():
                if self.is_section_open is False:
                    self.blocker.release_screen()
                    self.is_section_open = True
            else:
                self.is_section_open = False
                self.blocker.block_screen()

