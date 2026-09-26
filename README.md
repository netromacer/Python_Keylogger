# Python_Keylogger

NOTE: This project should be used for authorized testing or educational purposes only. You are free to copy, modify and reuse the source code at your own risk.

## About
This is a simple keylogger program that is developed in Python for purely educational and fun project purposes. This was done on my own authorised machines that I own.

## What is a Keylogger?
A keylogger is a program that aims to capture user keystrokes in hopes to gain any sensitive information such as user accounts or credentals. Many keyloggers come in differnet shapes, size of complexities. In this case, it is a simple Python script that has no intent to obsfucate itself as it is purely for demostration purposes.

## How is Works?
The program works via using the pynput module and it first defines a variable named logger_file which is equal to an open file named "keylog.txt" in append mode. This is followed by a function named on_press and takes a key as its parameter. The on_press function will try to write the key stroke in the keylog.txt file and will catch an attribute error if it captures a special key keystroke. Finally the program ultilises Listener to listen any keystrokes and if a key is pressed, it will run the on_press function.

## How to install
1. To install the keylogger, simply copy `git clone https://github.com/netromacer/Python_Keylogger/` and paste into the terminal.
2. Go into the directory and run `pip install -r requirements.txt` to install the required dependencies.
3. Run the program using `python3 keylogger.py`.

## Ethical Considerations
There are many ethical considerations when using a keylogger, for example there is a violation to personal privacy as business may implement a type of logging technology to track their employees or in extreme cases, a government that intentionaly tracks their citazen's devices (such as the infamous Red Star OS).

Another point of ethical consideration is the legal perspective, since this can be classified as malware it is unethical to run this without permission of the owner or to use on their devices. Running this without thier permission could potentially live **YOU** the potential to be charged with cybercrime. 

As I stated above, this is purely for educational purpose only and I am not legally responsible for any damage you may cause running this program.
