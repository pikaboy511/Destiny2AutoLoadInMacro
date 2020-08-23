import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener,KeyCode

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    def start_clicking(self):
        self.running = True
        print("program is running")

    def stop_clicking(self):
        self.running = False
        print("program has stopped")
    def exit(self):
        self.stop_clicking()
        self.program_running = False
        print("program has closed")

    def run(self):
         while self.program_running:
             while self.running:
                mouse.position = (1010,915)
                time.sleep(1)
                mouse.click(Button.left, 1)
                 time.sleep(1)
                mouse.position = (1019,634)
                 time.sleep(1)
                mouse.click(Button.left, 1)
                 time.sleep(1)
                mouse.position(122, 1064)
                time.sleep(5)
                mouse.position(971,314)
                time.sleep(1)
                mouse.click(Button.left, 1)
                time.sleep(1)
                mouse.position(1554,960)
                mouse.click(Button.left, 1)
                 time.sleep(75)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
     if key == start_stop_key:
         if click_thread.running:
             click_thread.stop_clicking()
         else:
             click_thread.start_clicking()
     elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()






