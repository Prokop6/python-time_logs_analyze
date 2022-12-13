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
    with open(f"run_times-{input_data['day']}.txt","a", encoding="utf8") as file:
        print("file created")

        file.write(f"Run time analisys for {input_data['day']}\n\n\n")


        file.write("\tStart of check,\tDuration\n")
        for t, d in zip(input_data['check_time'], input_data['check_dura']):
            file.write(f"\t{t},\t{d}\n")
