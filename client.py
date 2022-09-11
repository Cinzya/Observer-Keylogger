from pynput.keyboard import Listener

def on_press(key): # The function that's called when a key is pressed
    print("Key pressed: {0}".format(key))

def on_release(key): # The function that's called when a key is released
    print("Key released: {0}".format(key))


with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
    listener.join()  # Join the listener thread to the main thread to keep waiting for keys
