import cv2
import window
import login
import globals_config as gb
import time



class Session_Manager:
    def __init__(self) -> None:
        self.is_section_open = True
        self.authenticator = login.Authenticator()
        self.blocker = window.Blocker()
    def mainloop(self):
        cap = cv2.VideoCapture(0)
        try:
            while True:
                time.sleep(gb.config["delay"])
                # Read a frame from the webcam
                ret, frame = cap.read()
                
                # Convert the frame to grayscale
                #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                self.authenticator.verify_using_camera(frame)

                if self.authenticator.is_verified_now():
                    if self.is_section_open is False:
                        self.blocker.release_screen()
                        self.is_section_open = True
                else:
                    if self.is_section_open is True:
                        self.blocker.block_screen()
                    self.is_section_open = False
                print(str(self.authenticator.verified) + time.strftime("%H:%M:%S", time.localtime()))

        except KeyboardInterrupt:
            cap.release()

