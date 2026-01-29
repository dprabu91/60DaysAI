import pyautogui
import time


# Mouse Operations
'''
pyautogui.moveTo(100, 100, duration=1)  # Move mouse to (100, 100) over 1 second
time.sleep(1)  # Pause for a second
pyautogui.moveRel(200, 0, duration=1)  # Move
time.sleep(1)  # Pause for a second
pyautogui.click()  # Click at the current mouse position


pyautogui.rightClick(100, 100)  # Right-click at (100, 100

time.sleep(10)  # Pause for 10 seconds to observe the action

#x,y= pyautogui.position()  # Get the current mouse position

#print(f"Current mouse position: ({x}, {y})")

pyautogui.doubleClick(5046,15)


pyautogui.scroll(-500)  # Scroll down 500 units

pyautogui.drag(100,100,200,200, duration=1)  # Drag mouse to (200, 200) over 1 second

'''
# Keyboard Operations


time.sleep(5)  # Pause for 5 seconds to switch to the target application

x,y = pyautogui.position()  # Get the current mouse position

print(f"Current mouse position: ({x}, {y})")

time.sleep(5)  # Pause for 5 seconds to switch to the target application

pyautogui.click(x, y)  # Click at the current mouse position
time .sleep(1)  # Short pause before typing
pyautogui.write('Hello, World!', interval=0.1)  # Type with a delay of 0.1 seconds between each character
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'a')  # Simulate pressing Ctrl+S to save