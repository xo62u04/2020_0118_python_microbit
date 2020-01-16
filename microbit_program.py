from microbit import *
import radio

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('Hi') 
        
    incoming = radio.receive()
    if incoming == 'Hi':
        display.show('Hello', delay=300, wait=False, loop=False, clear=True)