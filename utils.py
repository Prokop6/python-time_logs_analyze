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


def write_to_txt(input_data: dict):
    '''writes input to a file'''
    with open(f"run_times-{input_data['day']}.txt","x", encoding="utf8"):
        print("file created")
