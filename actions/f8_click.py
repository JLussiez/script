import pyautogui
import time

def handle_f8():
    print("F8 : Détection de 'test.png' => Clic sur 'test2.png'")
    time.sleep(1)

    try:
        detection = pyautogui.locateOnScreen('test.png', confidence=0.8)
        if detection:
            print("✅ 'test.png' détecté !")

            target = pyautogui.locateOnScreen('test2.png', confidence=0.8)
            if target:
                center = pyautogui.center(target)
                pyautogui.moveTo(center.x, center.y, duration=0.5)
                pyautogui.click()
                print("🖱️ Clique effectué sur 'test2.png'")
            else:
                print("❌ 'test2.png' introuvable.")
        else:
            print("❌ 'test.png' non détecté.")
    except Exception as e:
        print("Erreur F8 :", e)
