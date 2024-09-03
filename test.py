import pyautogui
import random
import time

duration = 10
end_time = time.time() + duration

while time.time() < end_time:
    screen_width, screen_height = pyautogui.size()

    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)

    pyautogui.moveTo(x, y, duration=0.1)

    time.sleep(0.01)
