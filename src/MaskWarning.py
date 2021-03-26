from playsound import playsound
import datetime

class MaskWarning:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def play_sound(self, state):
        difference = int((self.start_time - self.end_time).total_seconds())  
        if difference > 10:
            if state == "mask":
                playsound('./utility/thanks_wear_mask.mp3')
                print("face detected")
            else:
                playsound('./utility/please_wear_mask.mp3')
                print("no face detected")

            new_end_time = datetime.datetime.now()
            return new_end_time
        else:
            return self.end_time

        
