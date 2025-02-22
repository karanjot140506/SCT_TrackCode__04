from pynput import keyboard # type: ignore
import time

def on_key_press(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # Display output in terminal
    print(f"{timestamp} - {key}")

    # Save to file
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {key}\n")

def main():
    user_word = input("Enter a word to track keystrokes: ")  # User enters a word
    print(f"Start typing '{user_word}' now. Press Ctrl+C to stop.")

    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
