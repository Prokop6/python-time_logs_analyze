"""
takes a list of file names and returns a list of contents
"""

def read_files(input_data: list[str]) -> list[str]:
    '''returns contents of a list of files'''
    data = []
    for file in input_data:
        with open(file, "rt", encoding="utf8") as input_dat:
            content = input_dat.read()
            data.append(content)
    return data
