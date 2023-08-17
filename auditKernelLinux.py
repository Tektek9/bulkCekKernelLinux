import pyautogui
import time
from termcolor import colored
target = ["namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver","namaserver"]
try:
    pyautogui.click(446, 68)
    pyautogui.write('https://teleport.domain.tld/')
    pyautogui.press('enter')
    time.sleep(13)
    pyautogui.click(962, 627)
    pyautogui.click(965, 619)
    time.sleep(5)
    pyautogui.click(470, 274)
    for wakwaw in target:
        pyautogui.click(470, 274)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.write(f'{str(wakwaw)}')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(1813, 348)
        pyautogui.click(1733, 410)
        time.sleep(5)
        pyautogui.click(658, 538)
        time.sleep(5)
        pyautogui.write('yum check-update kernel* && uname -r')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'shift', 'tab')
except KeyboardInterrupt:
    print(colored("Aplikasi mandek y, soale dicancel dewe", "magenta"))