#!/usr/bin/env python3

import sys, getopt
from plotwisetools import application

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv, "hf:d", ["help", "file="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-d':
            global _debug
            _debug = 1          
        elif opt in ("-f", "--file"):
            file = arg

    source = "".join(args[2])
    application.main(source)
