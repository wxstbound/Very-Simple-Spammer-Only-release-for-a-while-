import time
import pyautogui

msg = input("Enter the message to type: ")

while True:
    n = input("Enter the number of times to type the message (must be a positive integer): ")
    if n.isdigit() and int(n) > 0:
        break
    print("\033[1;31;40m INVALID INTEGER... EXITING")
    time.sleep(3)
    exit()

print("\033[3;31;40m Three second countdown starting. To end process drag your cursor to the top left of your screen.")
count = 3
while count != 0:
    print(count)
    time.sleep(1)
    count -= 1

print("\033[1;31;40m Starting...")

for i in range(int(n)):
    pyautogui.typewrite(msg + '\n')

  
  #Watch Youtube videos on how to install 'pyautogui'. Python installation here, https://www.python.org/downloads/.
  #Only thing I'll release because I like gatekeeping. Possibly release one that works remotely for multiple systems.
  