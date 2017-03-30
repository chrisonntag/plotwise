#!/usr/bin/env python3

import sys
from plotwisetools import application

if __name__ == "__main__":
    try:
        application.main(sys.argv[1])
    except IndexError:
        print("No *.csv file given. Enter file path.")
