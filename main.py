#!/usr/bin/env python3

# Clicker Bot

import pyautogui
import os, sys

# Clear the terminal
def clear():
    os.system('cls')

# Move to x,y coordinates and click
def moveClick(x,y,t):
    pyautogui.click(x,y,duration=t)

# Main function
def main():
    # Get file path to coordinates.txt
    filePath = os.path.join(sys.path[0], 'coordinates.txt')

    # Open and read coordinates.txt into array 'lines'
    with open(filePath, 'r') as f:
        lines = f.readlines()

    # Read each element in 'lines'
    for line in lines:
        # Remove '\n'
        x,y,t = line.replace('\n','').split(',')
        moveClick(int(x),int(y),float(t))


if __name__ == '__main__':
    # Clear the terminal
    clear()

    # Call main function
    main()