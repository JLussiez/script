import pyautogui
import time

def handle_f6():
    print("Action F6 : recherche 'test.png'")
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen('test.png', confidence=0.8)
        if location:
            center = pyautogui.center(location)
            pyautogui.moveTo(center.x, center.y, duration=0.5)
            pyautogui.click()
            print("Image cliquée.")
        else:
            print("Image 'test.png' non trouvée.")
    except Exception as e:
        print("Erreur F6 :", e)
