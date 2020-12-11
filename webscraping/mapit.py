# mapit.py- tool to search physical addresses
# usage -- python mapit.py 6600 Williams Road Richmond
# should take us to the address in google maps

import webbrowser
import sys

address = " ".join(sys.argv[1:])

prefix = "https://google.com/maps/place/"
webbrowser.open(prefix+address)

# TODO: add feature to grab address from clipboard
