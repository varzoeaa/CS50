import cowsay
import sys
from saying import hello

if len(sys.argv) == 2:
    cowsay.say("Hello, my name is " + sys.argv[1])



