from playsound import playsound
import datetime
import threading
import numpy as np

class MaskWarning:
    def __init__(self, cooldown = 5, fps_bin = 15):
        self.fps_bin = fps_bin
        self.cooldown = cooldown
        self.thanked = True
        self.timestamp = 0
        self.prober = []

    def probe(self, isMaskOff):
        self.prober.append(isMaskOff)
        if len(self.prober) > self.fps_bin:
            self.play_with_cooldown(round(np.mean(self.prober)))

    def play_with_cooldown(self, maskOff):
        self.prober.clear()
        time = datetime.datetime.now().timestamp()
        if time - self.timestamp > self.cooldown:
            if not self.thanked and maskOff == False:
                threading.Thread(target=playsound, args=('./utility/thanks_wear_mask.mp3',), daemon=True).start()
                threading.Thread(target=print, args=('THANK YOU',), daemon=True).start()
                self.thanked = True
            elif maskOff == True:
                threading.Thread(target=playsound, args=('./utility/please_wear_mask.mp3',), daemon=True).start()
                threading.Thread(target=print, args=('WEAR A MASK!',), daemon=True).start()
                self.timestamp = time
                self.thanked = False