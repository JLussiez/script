import keyboard
from actions.f6_click import handle_f6
from actions.f7_click import handle_f7
from actions.f8_click import handle_f8

running = True

def stop_script():
    global running
    print("Arrêt du script demandé (F2).")
    running = False

def main():
    global running

    print("=== Script de reconnaissance d'image ===")
    print("F6 : Chercher 'test.png'")
    print("F7 : Chercher 'test2.png'")
    print("F8 : Chercher 'test.png et cliquer sur test2.png'")
    print("F2 : Quitter le script")
    print("Appuie sur une touche...")

    keyboard.add_hotkey('F6', handle_f6)
    keyboard.add_hotkey('F7', handle_f7)
    keyboard.add_hotkey('F8', handle_f8)
    keyboard.add_hotkey('F2', stop_script)

    try:
        while running:
            keyboard.read_event()
    except KeyboardInterrupt:
        pass

    print("Script terminé.")

if __name__ == "__main__":
    main()
