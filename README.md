# Pegasus Spyware

## Overview
**Pegasus Spyware** is a sophisticated tool designed to stealthily capture sensitive data from a target host. The spyware periodically collects keylogs, clipboard data, and screenshots, encrypts this data, converts it into image format, and transmits it to an attacker's server. Upon receiving the data, the attacker must decrypt it before viewing.

## Features
- **Keylogging**: Captures all keystrokes entered by the user on the target machine.
- **Clipboard Monitoring**: Records the clipboard content, including copied text and other data.
- **Screenshot Capture**: Periodically takes screenshots of the host's screen.
- **Data Encryption**: All captured data is securely encrypted before transmission to ensure confidentiality.
- **Image Conversion**: Encrypted data is converted into image format for enhanced security during transmission.
- **Secure Transmission**: Data is sent securely to the attacker's server for decryption and analysis.

## How It Works
1. **Data Capture**: The spyware collects keylogs, clipboard data, and screenshots from the target host.
2. **Data Encryption**: The captured data is encrypted using robust encryption algorithms.
3. **Image Conversion**: Encrypted data is converted into an image format.
4. **Data Transmission**: The image is transmitted to the attacker's server.
5. **Data Decryption**: The attacker decrypts the received image to retrieve the original data.

## Tech Stack
### Python
Python is the core programming language used to develop the spyware, offering flexibility and powerful libraries.

### Flask
Flask is a lightweight web framework used to manage server-side operations and handle data transmission.

### Numpy
Numpy is utilized for efficient numerical operations, particularly in the manipulation and processing of data before encryption.

### Linux
The spyware is designed to run on Linux environments, leveraging the OS's robust security and scripting capabilities.

### PyAutoGUI
PyAutoGUI is used for automating the capture of screenshots and other user interactions on the host system.

### Pyput
Pyput handles keylogging and event listening to capture user inputs from the host machine.

### Pyperclip
Pyperclip is employed to monitor and capture clipboard data from the target host.

### Cryptography
The Cryptography library provides robust encryption methods to securely encrypt the captured data before transmission.


