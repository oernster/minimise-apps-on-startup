import json
import sys
from time import sleep

import keyboard
import mouse
from pynput.mouse import Controller


class MinimiseOnLaunch(object):
    VERSION = '1.0.0'
    CONFIG = {}

    def __init__(self):
        if self.load_settings():
            print(f"Waiting for {self.CONFIG['TIME_VAL']} seconds, then minimising all open windows...")
            sleep(int(self.CONFIG['TIME_VAL']))
            self.run()

    def load_settings(self):
        with open('config.json', 'r') as f:
            self.CONFIG = json.loads(f.read())
            for k, v in self.CONFIG.items():
                if k == 'Version' and v != '1.0.0':
                    print(f"config.json file has incompatible version.  This software requires version: {self.VERSION}")
                    return False
            return True
                
    def run(self):
        current_mouse = Controller()
        position = [i for i in current_mouse.position]
        mouse.move(0, 0)
        mouse.press(button='left')
        mouse.release(button='left')
        keyboard.press_and_release('win+d')
        mouse.move(position[0], position[1])


if __name__ == '__main__':
    MinimiseOnLaunch()
