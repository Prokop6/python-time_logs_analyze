"""
Performs regexp analysis on supplied file and returns a scatterplot of data
"""

import sys
from utils.utils import read_files

def main(input_data: list[str]) -> list[str]:
    data = read_files(input_data)

    print(data)

if __name__ == "__main__":
    main(sys.argv[1:])
