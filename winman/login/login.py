import cv2
import time
from deepface import DeepFace
import globals_config as gb


class Authenticator:
    def __init__(self) -> None:
        self.verified = False
        self.reference_image = cv2.imread("test/dependencies/r.jpg")
        self.not_verified_count = 0
    def verify_using_camera(self, frame):
        try:
            if DeepFace.verify(frame, self.reference_image)['verified']:
                #print("yes" + time.strftime("%H:%M:%S", time.localtime()))
                self.verified = True
                self.not_verified_count = 0
            else:
                #print("no" + time.strftime("%H:%M:%S", time.localtime()))
                self.verified = False
                self.not_verified_count += 1
        except ValueError:
            #print("invalid" + time.strftime("%H:%M:%S", time.localtime()))
            self.verified = False
            self.not_verified_count += 1
    def is_verified_now(self):
        if self.not_verified_count > gb.config["forget"]:
            return False
        else:
            return True


