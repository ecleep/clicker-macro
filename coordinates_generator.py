#!/usr/bin/env python3

# Coordinates generator for clicker bot

from pynput import mouse
import os, sys
import time

# Define empty array
arrCoordinates = []
prevTime = time.time()

# Clear the terminal
def clear():
    os.system('cls')

# Detect position of mouse when clicked
def on_click(x, y, button, pressed):
    global prevTime

    # Detect when mouse is clicked
    if pressed:

        # Check if middle-mouse is clicked
        if str(button) == 'Button.middle':
            # Generate file path to coordinates.txt in this script's folder
            filePath = os.path.join(sys.path[0], 'coordinates.txt')

            # Write coordinates to coordinates.txt
            with open(filePath, 'w') as f:
                f.write('\n'.join('%s,%s,%s' % x for x in arrCoordinates))
                print('Coordinates saved at ' + filePath)

            # Stop listener
            return False

        # Print coordinates of cursor when clicked
        print(x, y)

        # Get time in between current click and previous click
        currTime = time.time()
        timeDiff = str(round((currTime - prevTime),2))
        prevTime = currTime
        print(timeDiff)

        # Define coordinates in tuple and append to array
        coordinates = (x,y,timeDiff)
        arrCoordinates.append(coordinates)

# Main function
def main():
    # Reminder for user
    print('Middle-Click to stop program')

    # Start listener by joining it to thread
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == '__main__':
    # Clear the terminal
    clear()
    
    # Call main function
    main()