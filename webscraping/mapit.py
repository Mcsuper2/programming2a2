# mapit.py- tool to search physical addresses
# usage -- python mapit.py 6600 Williams Road Richmond
# should take us to the address in google maps

import webbrowser
import sys
import pyperclip

# If there are no arguments
# grab address from the clipboard
if len(sys.argv) < 2:
    address = pyperclip.paste()

else:
    address = " ".join(sys.argv[1:])

print(f"Finding {address}...")
prefix = "https://google.com/maps/place/"
webbrowser.open(prefix+address)


