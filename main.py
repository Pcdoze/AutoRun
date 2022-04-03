from tkinter import mainloop
from AutoRun import Runner
import keyboard, time

FRAMERATE = 30

def main_loop():
    loop = True

    runner = Runner()

    while loop:
        time.sleep(1/FRAMERATE)

        #________________

        print(runner.h_pressed)
        runner.run()
        
        #________________

        if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
            loop = False
main_loop()
