import keyboard, time


class Runner:
    def __init__(self):
        self.autorun = False
        self.h_pressed = 0
    
    def run(self):
        if keyboard.is_pressed('shift'):
            if keyboard.is_pressed('h') or keyboard.is_pressed('H'):
                self.h_pressed += 1
        else:
            self.h_pressed = 0

        if self.h_pressed == 1:
            if self.autorun:
                self.autorun = False
                keyboard.release('w')
            else:
                self.autorun = True

        if(self.autorun):
            keyboard.press('w')
