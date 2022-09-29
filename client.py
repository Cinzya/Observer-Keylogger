from pynput.keyboard import Listener
import configparser
import socket
import json

config = configparser.ConfigParser()
config.read('config.ini')

TCP_IP = config['COMPANION']['ip']
TCP_PORT = int(config['COMPANION']['port'])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Opening JSON file
f = open('commands.json')
data = json.load(f)
print(data)

# s.send(MESSAGE)

def on_press(key): # The function that's called when a key is pressed
    print("Key pressed: {0}".format(key))
    try: key.char
    except: return

    for keybind in data:
        if key.char == keybind['key']:
            s.send(keybind['command'].encode('utf-8')) # Send the command to the server
            s.send('\r\n'.encode('utf-8')) 
            print("Sent command: {0}".format(keybind['command'])) 


def on_release(key): # The function that's called when a key is released
    print("Key released: {0}".format(key))


with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
    listener.join()  # Join the listener thread to the main thread to keep waiting for keys

