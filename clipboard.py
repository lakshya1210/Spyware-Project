import pyperclip
import time
import requests

SERVER_URL = 'http://localhost:5000/upload_clipboard'

def monitor_clipboard():
    last_text = ""
    while True:
        try:
            text = pyperclip.paste()
            if text != last_text:
                print(f"Clipboard changed: {text[:30]}...")  # Show a preview of the text
                response = requests.post(SERVER_URL, json={'clipboard': text})
                if response.status_code == 200:
                    print("Clipboard data sent successfully.")
                else:
                    print(f"Failed to send clipboard data. Status code: {response.status_code}")
                last_text = text
            time.sleep(1)  # Check clipboard every second
        except Exception as e:
            print(f"Clipboard monitoring error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    monitor_clipboard()
