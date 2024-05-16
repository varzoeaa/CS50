import sys
import emoji

if len(sys.argv) != 2:
    sys.exit()

emojize(sys.argv[1])

def emojize(text):
    print("This is the emoji package" + emoji.emojize(text))
