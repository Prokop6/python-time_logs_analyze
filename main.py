#!/usr/bin/env python3

"""
Performs regexp analysis on supplied file and returns a scatterplot of data
"""

import sys
from utils.utils import read_files
import process

def main(input_data: list[str]) -> list[str]:
    data = read_files(input_data)

    processed_data = process.process(data)

    print(processed_data)

if __name__ == "__main__":
    main(sys.argv[1:])
