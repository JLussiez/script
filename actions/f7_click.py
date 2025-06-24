import pyautogui
import time

def handle_f7():
    print("Action F7 : recherche 'autre_image.png'")
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen('test2.png', confidence=0.8)
        if location:
            center = pyautogui.center(location)
            pyautogui.moveTo(center.x, center.y, duration=0.5)
            pyautogui.click()
            print("Image cliquée.")
        else:
            print("Image 'test2.png' non trouvée.")
    except Exception as e:
        print("Erreur F7 :", e)
