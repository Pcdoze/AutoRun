from AutoRun import Runner
import keyboard, time

FRAMERATE = 122

def main_loop():
    loop = True

    runner = Runner()

    while loop:
        time.sleep(1/FRAMERATE)

        #________________

        runner.run()
        
        #________________

        if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
            loop = False

main_loop()