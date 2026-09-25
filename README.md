# Python_Keylogger

## About
This is a simple keylogger program that is developed in Python for purely educational and fun project purposes. This was done on my own authorised machines that I own.

## What is a Keylogger?
A keylogger is a program that aims to capture user keystrokes in hopes to gain any sensitive information such as user accounts or credentals. Many keyloggers come in differnet shapes, size of complexities. In this case, it is a simple Python script that has no intent to obsfucate itself as it is purely for demostration purposes.

## How is works?
The program works via using the pynput module and it first defines a variable named logger_file which is equal to an open file named "keylog.txt" in append mode. This is followed by a function named on_press and takes a key as its parameter. The on_press function will try to write the key stroke in the keylog.txt file and will catch an attribute error if it captures a special key keystroke. Finally the program ultilises Listener to listen any keystrokes and if a key is pressed, it will run the on_press function.
